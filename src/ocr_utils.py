"""
OCR utilities for converting PDF pages to images and running OCR.

Functions
- pdf_to_images(pdf_path, poppler_path, dpi=300, first_page=None, last_page=None)
- ocr_image_to_text(image, lang='hin')
- extract_text_from_pdf(pdf_path, poppler_path, dpi=300)
"""

from typing import List
from PIL import Image

def pdf_to_images(pdf_path: str, poppler_path: str, dpi: int = 300,
                  first_page: int = None, last_page: int = None) -> List[Image.Image]:
    """
    Convert PDF pages to PIL Image objects using pdf2image.
    Returns a list of images for the requested page range.
    """
    raise NotImplementedError

def ocr_image_to_text(image: Image.Image, lang: str = "hin") -> str:
    """
    Run pytesseract OCR on a PIL Image and return extracted text.
    """
    raise NotImplementedError

def extract_text_from_pdf(pdf_path: str, poppler_path: str, dpi: int = 300) -> List[str]:
    """
    Convert all pages to images and return a list of raw OCR strings (one per page).
    """
    raise NotImplementedError
