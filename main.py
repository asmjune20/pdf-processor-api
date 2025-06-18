from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, FileResponse
import shutil
import os
import time
import json
import uuid
from pathlib import Path
import tempfile
from typing import List, Optional
from datetime import datetime

# Import your PDF processing functions
from simple_pdf_processor import _process_pdf_with_engine

app = FastAPI(title="PDF Processor API", version="2.0.0")

# Create directories for file storage
UPLOAD_DIR = Path("uploads")
RESULTS_DIR = Path("results")
METADATA_DIR = Path("metadata")

for directory in [UPLOAD_DIR, RESULTS_DIR, METADATA_DIR]:
    directory.mkdir(exist_ok=True)

# In-memory storage for file metadata (in production, use a database)
file_registry = {}

def save_metadata(file_id: str, metadata: dict):
    """Save file metadata to disk"""
    metadata_file = METADATA_DIR / f"{file_id}.json"
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2, default=str)

def load_metadata(file_id: str) -> dict:
    """Load file metadata from disk"""
    metadata_file = METADATA_DIR / f"{file_id}.json"
    if metadata_file.exists():
        with open(metadata_file, 'r') as f:
            return json.load(f)
    return None

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "PDF Processor API v2.0 is running!", "status": "healthy"}

# ==================== ENDPOINT 1: UPLOAD ====================
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF file and get a unique file ID for processing
    
    Returns:
    - file_id: Unique identifier for the uploaded file
    - filename: Original filename
    - file_size: Size in bytes
    - upload_time: When the file was uploaded
    """
    
    # Validate file type
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    # Generate unique file ID
    file_id = str(uuid.uuid4())
    
    # Save file with unique name
    file_extension = Path(file.filename).suffix
    stored_filename = f"{file_id}{file_extension}"
    file_path = UPLOAD_DIR / stored_filename
    
    try:
        # Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Create metadata
        metadata = {
            "file_id": file_id,
            "original_filename": file.filename,
            "stored_filename": stored_filename,
            "file_path": str(file_path),
            "file_size": os.path.getsize(file_path),
            "upload_time": datetime.now().isoformat(),
            "status": "uploaded",
            "processed": False,
            "processing_results": None
        }
        
        # Save metadata
        save_metadata(file_id, metadata)
        file_registry[file_id] = metadata
        
        return {
            "file_id": file_id,
            "filename": file.filename,
            "file_size": metadata["file_size"],
            "upload_time": metadata["upload_time"],
            "status": "uploaded",
            "message": "File uploaded successfully. Use this file_id to process the PDF."
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")
    
    finally:
        file.file.close()

# ==================== ENDPOINT 2: PROCESS ====================
@app.post("/process/{file_id}")
async def process_pdf(
    file_id: str,
    extract_tables: bool = True,
    use_ocr: bool = True,
    ocr_engine: str = "rapidocr"
):
    """
    Process an uploaded PDF by file ID
    
    Parameters:
    - file_id: The unique ID returned from upload
    - extract_tables: Whether to extract tables (default: True)
    - use_ocr: Whether to use OCR (default: True)
    - ocr_engine: OCR engine to use (default: "rapidocr")
    
    Returns:
    - Processing status and results
    """
    
    # Load file metadata
    metadata = load_metadata(file_id)
    if not metadata:
        raise HTTPException(status_code=404, detail="File ID not found")
    
    file_path = Path(metadata["file_path"])
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Uploaded file not found on disk")
    
    # Create results directory for this file
    results_dir = RESULTS_DIR / file_id
    results_dir.mkdir(exist_ok=True)
    
    try:
        # Update status to processing
        metadata["status"] = "processing"
        metadata["processing_started"] = datetime.now().isoformat()
        save_metadata(file_id, metadata)
        
        start_time = time.time()
        
        # Process PDF with Docling
        processing_results = _process_pdf_with_engine(
            file_path,
            results_dir,
            ocr_engine,
            force_full_page_ocr=True
        )
        
        processing_time = time.time() - start_time
        
        # Update metadata with results
        metadata.update({
            "status": "completed",
            "processed": True,
            "processing_completed": datetime.now().isoformat(),
            "processing_time": round(processing_time, 2),
            "processing_settings": {
                "extract_tables": extract_tables,
                "use_ocr": use_ocr,
                "ocr_engine": ocr_engine,
                "force_full_page_ocr": True
            },
            "processing_results": {
                "tables_found": processing_results.get('tables', 0),
                "text_file": str(processing_results.get('text_file', '')) if processing_results.get('text_file') else None,
                "results_directory": str(results_dir)
            }
        })
        
        save_metadata(file_id, metadata)
        file_registry[file_id] = metadata
        
        # List generated files
        result_files = list(results_dir.glob("*"))
        file_list = [{"filename": f.name, "size": f.stat().st_size} for f in result_files if f.is_file()]
        
        return {
            "file_id": file_id,
            "original_filename": metadata["original_filename"],
            "status": "completed",
            "processing_time": processing_time,
            "settings": metadata["processing_settings"],
            "results": {
                "tables_found": processing_results.get('tables', 0),
                "files_generated": len(file_list),
                "generated_files": file_list
            },
            "message": "PDF processed successfully. Use /retrieve/{file_id} to download results."
        }
        
    except Exception as e:
        # Update status to failed
        metadata.update({
            "status": "failed",
            "processing_error": str(e),
            "processing_failed": datetime.now().isoformat()
        })
        save_metadata(file_id, metadata)
        file_registry[file_id] = metadata
        
        raise HTTPException(status_code=500, detail=f"Failed to process PDF: {str(e)}")

# ==================== ENDPOINT 3: RETRIEVE ====================
@app.get("/retrieve/{file_id}")
async def retrieve_results(file_id: str, file_type: str = "summary"):
    """
    Retrieve processing results by file ID
    
    Parameters:
    - file_id: The unique ID from upload
    - file_type: Type of result to retrieve
      - "summary": JSON summary of processing results
      - "text": Processed text file
      - "tables": All table files (CSV/HTML)
      - "all": All generated files as zip
    
    Returns:
    - Requested files or summary
    """
    
    # Load file metadata
    metadata = load_metadata(file_id)
    if not metadata:
        raise HTTPException(status_code=404, detail="File ID not found")
    
    if not metadata.get("processed", False):
        raise HTTPException(status_code=400, detail="File has not been processed yet. Use /process/{file_id} first.")
    
    results_dir = RESULTS_DIR / file_id
    if not results_dir.exists():
        raise HTTPException(status_code=404, detail="Results directory not found")
    
    if file_type == "summary":
        # Return processing summary
        result_files = list(results_dir.glob("*"))
        file_list = [{"filename": f.name, "size": f.stat().st_size, "path": str(f)} for f in result_files if f.is_file()]
        
        return {
            "file_id": file_id,
            "original_filename": metadata["original_filename"],
            "status": metadata["status"],
            "upload_time": metadata["upload_time"],
            "processing_time": metadata.get("processing_time", 0),
            "settings": metadata.get("processing_settings", {}),
            "results": metadata.get("processing_results", {}),
            "generated_files": file_list,
            "download_instructions": {
                "text_file": f"/retrieve/{file_id}?file_type=text",
                "table_files": f"/retrieve/{file_id}?file_type=tables",
                "all_files": f"/retrieve/{file_id}?file_type=all"
            }
        }
    
    elif file_type == "text":
        # Return the main text file
        text_files = list(results_dir.glob("*_full_text_*.md"))
        if not text_files:
            raise HTTPException(status_code=404, detail="No text file found")
        
        return FileResponse(
            path=text_files[0],
            filename=f"{metadata['original_filename']}_extracted_text.md",
            media_type="text/markdown"
        )
    
    elif file_type == "tables":
        # Return first table file (could be enhanced to return all tables)
        table_files = list(results_dir.glob("*-table-*.csv"))
        if not table_files:
            raise HTTPException(status_code=404, detail="No table files found")
        
        return FileResponse(
            path=table_files[0],
            filename=f"{metadata['original_filename']}_table_1.csv",
            media_type="text/csv"
        )
    
    elif file_type == "all":
        # Create zip file with all results (simplified - just return file list for now)
        result_files = list(results_dir.glob("*"))
        file_info = []
        
        for f in result_files:
            if f.is_file():
                file_info.append({
                    "filename": f.name,
                    "size": f.stat().st_size,
                    "download_url": f"/retrieve/{file_id}/file/{f.name}"
                })
        
        return {
            "file_id": file_id,
            "all_files": file_info,
            "note": "Use individual file download URLs to get specific files"
        }
    
    else:
        raise HTTPException(status_code=400, detail="Invalid file_type. Use: summary, text, tables, or all")

# ==================== BONUS: INDIVIDUAL FILE DOWNLOAD ====================
@app.get("/retrieve/{file_id}/file/{filename}")
async def download_file(file_id: str, filename: str):
    """Download a specific file from processing results"""
    
    metadata = load_metadata(file_id)
    if not metadata:
        raise HTTPException(status_code=404, detail="File ID not found")
    
    file_path = RESULTS_DIR / file_id / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(path=file_path, filename=filename)

# ==================== UTILITY ENDPOINTS ====================
@app.get("/status/{file_id}")
async def get_file_status(file_id: str):
    """Get current status of a file"""
    
    metadata = load_metadata(file_id)
    if not metadata:
        raise HTTPException(status_code=404, detail="File ID not found")
    
    return {
        "file_id": file_id,
        "original_filename": metadata["original_filename"],
        "status": metadata["status"],
        "processed": metadata.get("processed", False),
        "upload_time": metadata["upload_time"],
        "processing_time": metadata.get("processing_time", None)
    }

@app.get("/list-files")
async def list_all_files():
    """List all uploaded files and their status"""
    
    files = []
    for file_id, metadata in file_registry.items():
        files.append({
            "file_id": file_id,
            "filename": metadata["original_filename"],
            "status": metadata["status"],
            "upload_time": metadata["upload_time"],
            "processed": metadata.get("processed", False)
        })
    
    return {"files": files, "total_files": len(files)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)