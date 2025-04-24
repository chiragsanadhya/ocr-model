from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Multi-Modal OCR API"
    
    # Processing
    MAX_IMAGE_SIZE: int = 1920  # Maximum dimension
    CONFIDENCE_THRESHOLD: float = 0.5
    
    # OCR Settings
    LANGUAGES: list = ["en"]  # Languages to detect
    
    class Config:
        case_sensitive = True

settings = Settings()