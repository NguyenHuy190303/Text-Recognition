from model import load_ocr_model
from preprocessing import preprocess_image
import torch

# Example function for OCR inference
def recognize_text(image_path):
    """Perform OCR on an image."""
    model = load_ocr_model()
    image = preprocess_image(image_path)

    # Convert image to tensor
    image_tensor = torch.tensor(image, dtype=torch.float32).unsqueeze(0).unsqueeze(0)

    # Predict (dummy output)
    with torch.no_grad():
        output = model(image_tensor)
    
    return "Recognized Text Placeholder"  # Replace with actual OCR output
