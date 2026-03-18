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
        results = self.reader.readtext(image_np) # testing with raw vs preprocessed image (Comparing confidence and processing time, thats why some commits have raw(image_np) or some have preprocessed image)

        ocr_result = []
        total_conf = 0.0

        for (bbox, text, conf) in results:
            conf = float(conf)
            total_conf += conf
            ocr_result.append({
                "text": str(text),
                "confidence": total_conf,
                "bbox": [[int(x), int(y)] for (x, y) in bbox]
            })
        
        endTime= time.perf_counter()

        avg_conf = total_conf/ len(results)


        return {
            "processing_time": round(endTime - startTime,3),
            "avg_confidence": avg_conf,
            "results": ocr_result,
    
        }
    
ocr_service = OCRService()