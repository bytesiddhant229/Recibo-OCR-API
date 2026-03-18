import easyocr
import numpy as np
from PIL import Image
import io
import time
from services.preprocess import preprocess_image


class OCRService:
    def __init__(self):
        self.reader = easyocr.Reader(["en"], gpu=True) # setting up reader n enabling GPU

    def load_image(self, image_bytes: bytes):
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        return np.array(image)
    
    def extract_text(self, image_bytes:bytes):
        startTime = time.perf_counter()
        image_np = self.load_image(image_bytes)

        preprocessedImage = preprocess_image(image_np) 
        results = self.reader.readtext(preprocessedImage) # totally forgot to add preprocessed image for ocr, lol - 19-03-26

        ocr_result = []

        for (bbox, text, conf) in results:
            ocr_result.append({
                "text": str(text),
                "confidence": float(conf),
                "bbox": [[int(x), int(y)] for (x, y) in bbox]
            })
        
        endTime= time.perf_counter()

        return {
            "processing_time": round(endTime - startTime,3),
            "results": ocr_result,
    
        }
    
ocr_service = OCRService()