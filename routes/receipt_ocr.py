from fastapi import APIRouter, UploadFile, File
from services.ocr_service import ocr_service

router = APIRouter()




@router.post("/")
async def run_ocr(file: UploadFile = File(...)):
    contents = await file.read()

    results = ocr_service.extract_text(contents)

    return {
        "filename": file.filename,
        "processing_time": results["processing_time"],
        "avg_confidence": results["avg_confidence"],
        "results": results["results"]
    }