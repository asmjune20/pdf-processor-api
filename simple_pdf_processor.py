# Simple PDF Processing Script - One Function
# Processes PDFs with 4 OCR engines × 2 force settings each (now includes OCRMac)

import os
import time
import signal
from pathlib import Path

# Set Tesseract environment
os.environ['TESSDATA_PREFIX'] = '/opt/homebrew/share/tessdata'
os.environ['PATH'] = os.environ['PATH'] + ':/opt/homebrew/bin'

from docling_core.types.doc import ImageRefMode, PictureItem, TableItem
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions, 
    TesseractOcrOptions,
    EasyOcrOptions,
    RapidOcrOptions,
    OcrMacOptions
)
from docling.document_converter import DocumentConverter, PdfFormatOption

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("OCR operation timed out")

def run_with_timeout(func, timeout_seconds, *args, **kwargs):
    old_handler = signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)
    try:
        result = func(*args, **kwargs)
        signal.alarm(0)
        return result
    except TimeoutError:
        raise TimeoutError(f"Function timed out after {timeout_seconds} seconds")
    finally:
        signal.signal(signal.SIGALRM, old_handler)

def _process_pdf_with_engine(pdf_path, output_dir, ocr_engine, force_full_page_ocr):
    """Process single PDF with specific OCR engine and force setting"""
    
    # Configure pipeline
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.do_cell_matching = True
    pipeline_options.do_ocr = True
    
    # Set OCR engine
    if ocr_engine == "easyocr":
        ocr_options = EasyOcrOptions(force_full_page_ocr=force_full_page_ocr)
    elif ocr_engine == "tesseract":
        ocr_options = TesseractOcrOptions(force_full_page_ocr=force_full_page_ocr, lang=["auto"])
    elif ocr_engine == "rapidocr":
        ocr_options = RapidOcrOptions(force_full_page_ocr=force_full_page_ocr)
    elif ocr_engine == "ocrmac":
        ocr_options = OcrMacOptions(force_full_page_ocr=force_full_page_ocr)
    else:
        raise ValueError(f"Unsupported OCR engine: {ocr_engine}")
    
    pipeline_options.ocr_options = ocr_options
    
    # Initialize converter
    doc_converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )
    
    # Convert document
    conv_res = doc_converter.convert(str(pdf_path))
    
    if conv_res is None:
        raise Exception("Failed to convert document")
    
    doc_filename = pdf_path.stem
    
    # Extract tables
    if conv_res.document.tables:
        for table_ix, table in enumerate(conv_res.document.tables):
            table_df = table.export_to_dataframe()
            csv_filename = Path(output_dir) / f"{doc_filename}-table-{table_ix + 1}.csv"
            table_df.to_csv(csv_filename, index=False)
            
            html_filename = Path(output_dir) / f"{doc_filename}-table-{table_ix + 1}.html"
            with html_filename.open("w") as fp:
                fp.write(table.export_to_html(doc=conv_res.document))
    
    # Extract full text
    full_text = conv_res.document.export_to_markdown()
    force_suffix = "force_true" if force_full_page_ocr else "force_false"
    text_filename = Path(output_dir) / f"{doc_filename}_full_text_{ocr_engine}_{force_suffix}.md"
    with text_filename.open("w", encoding="utf-8") as fp:
        fp.write(full_text)
    
    return {
        'tables': len(conv_res.document.tables) if conv_res.document.tables else 0,
        'text_file': text_filename
    }

def process_pdfs_all_engines(folder_path="/Users/june/Downloads/docling"):
    """
    Automatically find and process ALL PDFs in a folder with 4 OCR engines and both force settings
    
    Args:
        folder_path: Path to folder containing PDFs (will find all .pdf files automatically)
        
    Returns:
        Dictionary with results and timing data
    """
    
    OCR_ENGINES = ['rapidocr', 'tesseract', 'easyocr', 'ocrmac']
    FORCE_SETTINGS = [True, False]
    TIMEOUT = 600  # 10 minutes per processing
    
    base_folder = Path(folder_path)
    
    # Automatically find all PDF files in the folder
    if not base_folder.exists():
        print(f"❌ Folder not found: {folder_path}")
        return {}
    
    pdf_files = list(base_folder.glob("*.pdf"))
    if not pdf_files:
        print(f"❌ No PDF files found in: {folder_path}")
        return {}
    
    # Convert to just filenames
    existing_files = [pdf.name for pdf in pdf_files]
    
    print(f"🚀 Found {len(existing_files)} PDFs to process with 4 engines × 2 settings = {len(existing_files) * 8} total runs")
    print(f"📁 Folder: {folder_path}")
    print(f"📄 PDFs found:")
    for pdf in existing_files:
        print(f"   • {pdf}")
    print(f"{'='*80}")
    
    all_results = {}
    timing_data = {}
    total_start_time = time.time()
    
    # Process each PDF
    for i, pdf_filename in enumerate(existing_files):
        print(f"\n📄 PDF {i+1}/{len(existing_files)}: {pdf_filename}")
        print("="*60)
        
        pdf_path = base_folder / pdf_filename
        pdf_stem = pdf_path.stem
        timing_data[pdf_filename] = {}
        
        # Process with each engine and force setting
        for ocr_engine in OCR_ENGINES:
            timing_data[pdf_filename][ocr_engine] = {}
            
            for force_setting in FORCE_SETTINGS:
                force_label = "force_true" if force_setting else "force_false"
                
                print(f"\n🔍 {ocr_engine} (force={force_setting})")
                
                try:
                    # Create output folder: name_engine_force_setting
                    output_folder = base_folder / f"{pdf_stem}_{ocr_engine}_{force_label}"
                    output_folder.mkdir(parents=True, exist_ok=True)
                    
                    start_time = time.time()
                    
                    # Process with timeout
                    result = run_with_timeout(
                        _process_pdf_with_engine,
                        TIMEOUT,
                        pdf_path, output_folder, ocr_engine, force_setting
                    )
                    
                    duration = time.time() - start_time
                    
                    # Store results
                    result_key = f"{pdf_filename}_{ocr_engine}_{force_label}"
                    all_results[result_key] = result
                    timing_data[pdf_filename][ocr_engine][force_label] = duration
                    
                    print(f"   ✅ {duration:.1f}s - {result['tables']} tables")
                    
                except Exception as e:
                    duration = time.time() - start_time if 'start_time' in locals() else 0
                    print(f"   ❌ FAILED ({duration:.1f}s): {str(e)[:50]}...")
                    
                    result_key = f"{pdf_filename}_{ocr_engine}_{force_label}"
                    all_results[result_key] = {"error": str(e)}
                    timing_data[pdf_filename][ocr_engine][force_label] = f"FAILED ({duration:.1f}s)"
    
    total_duration = time.time() - total_start_time
    
    # Print final summary
    print(f"\n{'='*80}")
    print(f"🎉 PROCESSING COMPLETE")
    print(f"⏱️  Total time: {total_duration:.1f} seconds ({total_duration/60:.1f} minutes)")
    print(f"{'='*80}")
    
    # Print timing comparison for each engine
    for engine in OCR_ENGINES:
        print(f"\n🔍 {engine.upper()} RESULTS:")
        print("="*60)
        print(f"{'PDF Name':<40} {'Force=True':<12} {'Force=False':<12} {'Speedup':<8}")
        print("-"*72)
        
        for pdf_name in existing_files:
            short_name = pdf_name[:37] + "..." if len(pdf_name) > 40 else pdf_name
            
            timings = timing_data.get(pdf_name, {}).get(engine, {})
            true_time = timings.get('force_true', 'N/A')
            false_time = timings.get('force_false', 'N/A')
            
            if isinstance(true_time, (int, float)) and isinstance(false_time, (int, float)):
                speedup = f"{true_time/false_time:.1f}x" if false_time > 0 else "N/A"
                true_str = f"{true_time:.1f}s"
                false_str = f"{false_time:.1f}s"
            else:
                speedup = "N/A"
                true_str = str(true_time)[:11]
                false_str = str(false_time)[:11]
            
            print(f"{short_name:<40} {true_str:<12} {false_str:<12} {speedup:<8}")
    
    # Print folder summary
    print(f"\n📁 FOLDERS CREATED:")
    print("="*40)
    folder_count = 0
    for pdf_name in existing_files:
        pdf_stem = Path(pdf_name).stem
        for engine in OCR_ENGINES:
            print(f"✅ {pdf_stem}_{engine}_force_true/")
            print(f"✅ {pdf_stem}_{engine}_force_false/")
            folder_count += 2
    
    print(f"\n📊 Total folders created: {folder_count}")
    
    return all_results, timing_data

# HOW TO USE:
# Just give it a folder path and it will process ALL PDFs in that folder!
#
# results, timings = process_pdfs_all_engines("/path/to/your/folder")
#
# That's it! No need to list individual filenames.

if __name__ == "__main__":
    print("📝 To use this script, just call it with a folder path:")
    print()
    print('results, timings = process_pdfs_all_engines("/path/to/your/folder")')
    print()
    print("🔍 It will automatically find and process ALL PDFs in that folder!")
    print("📁 Each PDF gets processed with 4 engines × 2 force settings = 8 folders per PDF")
    print()
    print("Example:")
    print('results, timings = process_pdfs_all_engines("/Users/june/Downloads/docling/New docling test")')