import time
from pathlib import Path
import numpy as np
import cv2
from PIL import Image
import io
from typing import List, Tuple
import easyocr
from ..config import settings

class OCRService:
    def __init__(self):
        # Initialize EasyOCR reader
        self.reader = easyocr.Reader(settings.LANGUAGES)

    def preprocess_image(self, image):
        # Resize if image is too large
        h, w = image.shape[:2]
        if max(h, w) > settings.MAX_IMAGE_SIZE:
            scale = settings.MAX_IMAGE_SIZE / max(h, w)
            new_h, new_w = int(h * scale), int(w * scale)
            image = cv2.resize(image, (new_w, new_h))
        return image

    async def process_image(self, image_data: bytes) -> Tuple[List[dict], float]:
        start_time = time.time()
        
        # Convert bytes to numpy array
        nparr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        image = self.preprocess_image(image)
        
        # Perform OCR using EasyOCR
        results = self.reader.readtext(image)
        detections = []
        
        for bbox, text, confidence in results:
            if confidence < settings.CONFIDENCE_THRESHOLD:
                continue
                
            # EasyOCR returns points in format: [[x1,y1], [x2,y2], [x3,y3], [x4,y4]]
            x_min = min(point[0] for point in bbox)
            y_min = min(point[1] for point in bbox)
            x_max = max(point[0] for point in bbox)
            y_max = max(point[1] for point in bbox)
            
            detections.append({
                "text": text,
                "confidence": float(confidence),
                "bounding_box": {
                    "x": float(x_min),
                    "y": float(y_min),
                    "width": float(x_max - x_min),
                    "height": float(y_max - y_min)
                },
                "text_type": "text"  # EasyOCR doesn't differentiate between printed and handwritten
            })
        
        processing_time = time.time() - start_time
        return detections, processing_time