"""
Image processing utilities
"""

import io
from PIL import Image
from typing import Tuple

try:
    import pytesseract
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False

def get_image_dimensions(image_bytes: bytes) -> Tuple[int, int]:
    """Get image width and height."""
    image = Image.open(io.BytesIO(image_bytes))
    return image.size

def resize_image(image_bytes: bytes, max_width: int, max_height: int) -> bytes:
    """Resize image while maintaining aspect ratio."""
    image = Image.open(io.BytesIO(image_bytes))
    image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
    
    output = io.BytesIO()
    image.save(output, format='PNG')
    return output.getvalue()

def extract_text_ocr(image_bytes: bytes) -> str:
    """Extract text from image using OCR."""
    if not TESSERACT_AVAILABLE:
        raise Exception("Tesseract OCR is not installed. Please install pytesseract and tesseract-ocr.")
    
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    return text.strip()

def convert_to_format(image_bytes: bytes, format: str = 'PNG') -> bytes:
    """Convert image to specified format."""
    image = Image.open(io.BytesIO(image_bytes))
    output = io.BytesIO()
    image.save(output, format=format)
    return output.getvalue()