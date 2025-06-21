# PDF Processor API

A FastAPI-based service for extracting tables, images, and text from PDF files using [Docling](https://github.com/DS4SD/docling) with OCR capabilities.

## 🚀 Features

- **Table Extraction**: Extract tables as CSV and HTML files
- **Image Extraction**: Extract images as PNG files (**Working!**)
- **OCR Text Extraction**: Extract text with multiple OCR engines
- **Simple API**: Upload → Process → Download workflow
- **Multiple OCR Engines**: RapidOCR, Tesseract, EasyOCR, OCRMac
- **Configurable Processing**: Control OCR intensity and extraction options

## 📋 Requirements

- Python 3.8+
- Tesseract OCR (for tesseract engine)
- macOS recommended (for OCRMac engine)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/asmjune20/pdf-processor-api.git
cd pdf-processor-api
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Tesseract (Optional but Recommended)
**macOS:**
```bash
brew install tesseract
```

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr
```

**Windows:**
Download from: https://github.com/UB-Mannheim/tesseract/wiki

## 🚀 Quick Start

### 1. Start the Server
```bash
uvicorn main:app --reload
```

### 2. Open the API Interface
Navigate to: **http://localhost:8000/docs**

### 3. Use the Simple Workflow

#### 📤 Step 1: Upload PDF
- Go to `POST /upload-pdf/`
- Click "Try it out"
- Upload your PDF file
- Copy the returned `file_id`

#### ⚙️ Step 2: Process PDF
- Go to `POST /process-pdf/`
- Click "Try it out"
- Enter your `file_id`
- Configure options:
  - `extract_tables`: Get tables as CSV/HTML (default: true)
  - `extract_images`: Get images as PNG (default: true)
  - `force_full_page_ocr`: OCR intensity (default: true)
  - `ocr_engine`: Choose engine (default: "rapidocr")
- Click "Execute"

#### 📥 Step 3: Download Results
- Go to `GET /download-results/{file_id}`
- Enter your `file_id`
- Click "Execute" → "Download file"
- Get a ZIP with all extracted content

## 📁 Results Location

**Important**: Results are saved in the `uploads/` folder on your local system:

```
uploads/
├── [file-id].pdf                           # Your uploaded PDF
└── [file-id]_[engine]_[force-setting]/     # Processing results
    ├── [filename]-table-1.csv              # Table data
    ├── [filename]-table-1.html             # Table HTML
    ├── [filename]-picture-1.png            # Extracted images
    ├── [filename]-picture-2.png            # More images...
    └── [filename]_full_text_[engine]_[force].md  # OCR text
```

You can browse the `uploads/` folder directly or use the download endpoint to get everything as a ZIP file.

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/upload-pdf/` | POST | Upload PDF, get file_id |
| `/process-pdf/` | POST | Process PDF with options |
| `/download-results/{file_id}` | GET | Download results as ZIP |


## ⚙️ Processing Options

### `force_full_page_ocr`
- **`true`** (default): Thorough OCR on every page (slower, more complete)
- **`false`**: Smart OCR only where needed (faster, usually sufficient)

### `extract_tables` 
- **`true`** (default): Extract tables as CSV/HTML files
- **`false`**: Skip table extraction (faster)

### `extract_images`
- **`true`** (default): Extract images as PNG files  
- **`false`**: Skip image extraction (faster)

## 🐛 Troubleshooting

### Common Issues

**"No images found"**
- PDF may contain only vector graphics or text
- Try different OCR engines
- Some table image failures are normal (text tables become CSV instead)

**"Latin language warnings"**  
- These warnings are normal and can be ignored
- Tesseract detects Latin script but processing continues

**Slow processing**
- Try `force_full_page_ocr=false` for faster processing
- Use `rapidocr` engine for speed
- Disable unused features (`extract_images=false` if not needed)

**OCR engine failures**
- Different engines work better for different PDFs
- Try switching engines if one fails
- RapidOCR is most reliable as fallback

## 📝 Example API Usage

### Using the Web Interface
1. Start: `uvicorn main:app --reload`
2. Open: http://localhost:8000/docs
3. Upload → Process → Download

### Using curl
```bash
# 1. Upload PDF
curl -X POST "http://localhost:8000/upload-pdf/" \
  -F "file=@your-document.pdf"

# 2. Process PDF (replace YOUR_FILE_ID)
curl -X POST "http://localhost:8000/process-pdf/" \
  -G -d "file_id=YOUR_FILE_ID" \
  -d "extract_tables=true" \
  -d "extract_images=true" \
  -d "force_full_page_ocr=true" \
  -d "ocr_engine=rapidocr"

# 3. Download results
curl -X GET "http://localhost:8000/download-results/YOUR_FILE_ID" \
  -o results.zip
```

## 🎯 What's Fixed in v2.0

### ✅ Major Improvements
- **Image extraction now works properly** (added proper docling pipeline settings)
- **Simplified API** to 3 essential endpoints only
- **Clearer parameter names** (`use_ocr` → `force_full_page_ocr`)
- **Better file organization** (all results in `uploads/` folder)
- **ZIP download** for easy result collection

### 🔧 Technical Fixes
- Added `generate_picture_images=True` to docling pipeline
- Using `iterate_items()` method for proper image extraction
- Fixed table/image detection and saving
- Improved error handling and user feedback

## 📄 File Structure

**What gets uploaded to GitHub:**
```
pdf-processor-api/
├── main.py                    # FastAPI server
├── simple_pdf_processor.py    # PDF processing logic  
├── requirements.txt           # Dependencies
├── .gitignore                # Git ignore rules
└── README.md                 # This documentation
```

**What stays local (not uploaded):**
```
uploads/                      # Your PDFs and results
venv/                        # Virtual environment
metadata/                    # Docling cache
__pycache__/                 # Python cache
```

---

**Built with [Docling](https://github.com/DS4SD/docling) - Advanced document AI toolkit**
