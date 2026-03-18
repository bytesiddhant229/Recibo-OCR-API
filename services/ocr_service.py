import easyocr
import numpy as np
from PIL import Image
import io
import time


class OCRService:
    def __init__(self):
        self.reader = easyocr.Reader(["en"], gpu=True)

    def load_image(self, image_bytes: bytes):
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        return np.array(image)
    
    def extract_text(self, image_bytes:bytes):
        startTime = time.perf_counter()
        image_np = self.load_image(image_bytes)
        results = self.reader.readtext(image_np)

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