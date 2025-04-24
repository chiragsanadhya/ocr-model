from pydantic import BaseModel
from typing import List, Optional

class BoundingBox(BaseModel):
    x: float
    y: float
    width: float
    height: float

class TextDetection(BaseModel):
    text: str
    confidence: float
    bounding_box: BoundingBox
    text_type: str  # "printed" or "handwritten"

class OCRResponse(BaseModel):
    success: bool
    message: str
    detections: List[TextDetection]
    processing_time: float