import cv2
from PIL import Image
import numpy as np

# Example function for image preprocessing
def preprocess_image(image_path):
    """Load and preprocess an image for OCR."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (256, 256))
    _, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    return image
