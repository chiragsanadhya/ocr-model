from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from typing import List
import logging
from .services.ocr_service import OCRService
from .models import OCRResponse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Multi-Modal OCR API",
    description="API for processing both printed and handwritten text from images",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OCR service
ocr_service = OCRService()

@app.get("/")
async def root():
    return {"message": "Welcome to Multi-Modal OCR API"}

@app.post("/ocr/process", response_model=OCRResponse)
async def process_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        detections, processing_time = await ocr_service.process_image(contents)
        
        return OCRResponse(
            success=True,
            message="Image processed successfully",
            detections=detections,
            processing_time=processing_time
        )
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)