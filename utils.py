import os

# Example function to save results
def save_results(text, output_file="output.txt"):
    """Save OCR results to a file."""
    with open(output_file, "w") as f:
        f.write(text)

# Example function to load an image path
def load_image_path(folder):
    """Load all image paths from a folder."""
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
