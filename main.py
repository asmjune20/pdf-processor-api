from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.responses import JSONResponse, FileResponse
from pathlib import Path
import shutil
import uuid
import logging
import zipfile
import tempfile

# Import your PDF processor
from simple_pdf_processor import process_single_pdf

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Simple PDF Processing API",
    description="Upload PDF → Process PDF → Download Results",
    version="1.0.0"
)

# Configuration
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
async def root():
    return {
        "message": "Simple PDF Processing API",
        "version": "1.0.0",
        "workflow": "Upload PDF → Process PDF → Download Results",
        "endpoints": {
            "POST /upload-pdf/": "Upload a PDF file",
            "POST /process-pdf/": "Process uploaded PDF",
            "GET /download-results/{file_id}": "Download processing results"
        }
    }

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Step 1: Upload a PDF file and get a file_id
    """
    # Validate file type
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    if file.size == 0:
        raise HTTPException(status_code=400, detail="Empty file not allowed")
    
    try:
        # Generate unique file ID
        file_id = str(uuid.uuid4())
        
        # Save uploaded file
        file_path = UPLOAD_DIR / f"{file_id}.pdf"
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        logger.info(f"File uploaded: {file.filename} -> {file_id}")
        
        return {
            "file_id": file_id,
            "original_filename": file.filename,
            "size": file.size,
            "next_step": f"Use this file_id to process the PDF at /process-pdf/"
        }
        
    except Exception as e:
        logger.error(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

@app.post("/process-pdf/")
async def process_pdf(
    file_id: str = Query(..., description="File ID from upload-pdf"),
    extract_tables: bool = Query(True, description="Extract tables as CSV/HTML"),
    extract_images: bool = Query(True, description="Extract images as PNG"),
    force_full_page_ocr: bool = Query(True, description="Force OCR on all pages vs smart OCR"),
    ocr_engine: str = Query("rapidocr", description="OCR engine", enum=["rapidocr", "tesseract", "easyocr", "ocrmac"])
):
    """
    Step 2: Process the uploaded PDF with extraction options
    """
    
    # Check if file exists
    pdf_file_path = UPLOAD_DIR / f"{file_id}.pdf"
    if not pdf_file_path.exists():
        raise HTTPException(status_code=404, detail=f"File {file_id} not found. Please upload first.")
    
    try:
        logger.info(f"Processing: {file_id}")
        
        # Process the PDF
        result = process_single_pdf(
            pdf_filename=f"{file_id}.pdf",
            folder_path=str(UPLOAD_DIR),
            extract_tables=extract_tables,
            extract_images=extract_images,
            force_full_page_ocr=force_full_page_ocr,
            ocr_engine=ocr_engine
        )
        
        logger.info(f"Processing completed: {file_id}")
        
        return {
            "file_id": file_id,
            "status": "completed",
            "results": {
                "tables_count": result.get('tables', 0),
                "images_count": result.get('images', 0),
                "text_extracted": bool(result.get('text_file')),
                "output_folder": str(result.get('output_folder', ''))
            },
            "next_step": f"Download results at /download-results/{file_id}"
        }
        
    except Exception as e:
        logger.error(f"Processing failed for {file_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

@app.get("/download-results/{file_id}")
async def download_results(file_id: str):
    """
    Step 3: Download all processing results as a ZIP file
    """
    
    # Find the results folder
    result_folders = list(UPLOAD_DIR.glob(f"{file_id}_*"))
    
    if not result_folders:
        raise HTTPException(status_code=404, detail=f"No results found for {file_id}. Process the PDF first.")
    
    try:
        # Create a temporary ZIP file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as temp_zip:
            with zipfile.ZipFile(temp_zip.name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                
                # Add all files from all result folders
                for result_folder in result_folders:
                    if result_folder.is_dir():
                        folder_name = result_folder.name
                        
                        for file_path in result_folder.rglob('*'):
                            if file_path.is_file():
                                # Add file to ZIP with folder structure
                                arcname = f"{folder_name}/{file_path.relative_to(result_folder)}"
                                zipf.write(file_path, arcname)
        
        logger.info(f"Results packaged for download: {file_id}")
        
        # Return the ZIP file
        return FileResponse(
            path=temp_zip.name,
            filename=f"{file_id}_results.zip",
            media_type="application/zip"
        )
        
    except Exception as e:
        logger.error(f"Download failed for {file_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Download failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Simple PDF Processing API")
    print("📁 Workflow: Upload → Process → Download")
    print("📂 Upload folder:", UPLOAD_DIR.absolute())
    print()
    
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        log_level="info"
    )