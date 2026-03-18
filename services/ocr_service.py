import easyocr
import numpy as np
from PIL import Image
import io


class OCRService:
    def __init__(self):
        self.reader = easyocr.Reader(["en"], gpu=True)

    def load_image(self, image_bytes: bytes):
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        return np.array(image)
    
    def extract_text(self, image_bytes:bytes):
        image_np = self.load_image(image_bytes)
        results = self.reader.readtext(image_np)

        return [
            {
                "text":text,
                "confidence": float(conf),
                "bbox": [[int(x), int(y)] for (x, y) in bbox]
            }
            for (bbox, text, conf) in results
        ]
    
ocr_service = OCRService()