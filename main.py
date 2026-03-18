from fastapi import FastAPI
from routes import receipt_ocr

app = FastAPI()

app.include_router(receipt_ocr.router, prefix="/ocr", tags=["OCR"])

@app.get("/")
def root():
    return {"message": "Welcome to Recibo OCR API"}