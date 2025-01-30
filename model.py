import torch
import torchvision.models as models

# Example function for loading a model
def load_ocr_model():
    """Load a pre-trained OCR model (Example)."""
    model = models.resnet18(pretrained=True)
    model.fc = torch.nn.Linear(model.fc.in_features, 10)  # Example modification
    model.eval()
    return model
