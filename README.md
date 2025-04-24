# ocr-model



          
# Multi-Modal OCR System

A modern Optical Character Recognition (OCR) system built with FastAPI and Streamlit, capable of extracting text from both printed and handwritten content in images.

## 🌟 Features

- Fast and accurate text detection and recognition using EasyOCR
- Support for both printed and handwritten text
- Real-time text extraction with bounding box visualization
- User-friendly Streamlit web interface
- RESTful API endpoints with FastAPI
- Image preprocessing for optimal results
- Confidence scoring for detected text
- Multi-language support (currently configured for English)

## 🏗️ Project Structure
```
OCR project/
├── .env                 # Environment variables
├── .gitignore          # Git ignore rules
├── requirements.txt    # Project dependencies
└── src/
    ├── api/           # Backend API
    │   ├── config.py  # Configuration settings
    │   ├── services/
    │   │   └── ocr_service.py  # OCR implementation
    │   └── app.py     # FastAPI application
    └── frontend/      # Streamlit frontend
        └── app.py     # User interface
```

## 🚀 Technology Stack

- **Backend**: FastAPI - High-performance web framework
- **Frontend**: Streamlit - Interactive data app framework
- **OCR Engine**: EasyOCR - Efficient text detection and recognition
- **Image Processing**: OpenCV, Pillow
- **Data Validation**: Pydantic

## 📦 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd OCR\ project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🔧 Configuration

The system can be configured through environment variables:

- `MAX_IMAGE_SIZE`: Maximum image dimension (default: 1920)
- `CONFIDENCE_THRESHOLD`: Minimum confidence score (default: 0.5)
- `LANGUAGES`: List of languages to detect (default: ["en"])

## 🚀 Usage

1. Start the FastAPI backend:
```bash
uvicorn src.api.app:app --reload --host 0.0.0.0 --port 8000
```

2. Launch the Streamlit frontend:
```bash
streamlit run src/frontend/app.py
```

3. Access the application:
- Frontend UI: http://localhost:8501
- API Documentation: http://localhost:8000/docs

## 🔌 API Endpoints

### Welcome Endpoint
- **GET /** 
  - Returns: Welcome message

### OCR Processing Endpoint
- **POST /ocr/process**
  - Purpose: Process image and extract text
  - Accepts: Image file (PNG, JPEG)
  - Returns: JSON with detected text, confidence scores, and bounding boxes

## 💻 Development

The project uses:
- FastAPI for robust API development
- Streamlit for intuitive user interface
- EasyOCR for efficient text recognition
- Pydantic for data validation
- OpenCV and Pillow for image processing

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

Your Name - your.email@example.com
Project Link: [https://github.com/yourusername/ocr-project](https://github.com/yourusername/ocr-project)

## 🙏 Acknowledgments

- EasyOCR for providing the OCR engine
- FastAPI for the excellent web framework
- Streamlit for the amazing UI framework

        