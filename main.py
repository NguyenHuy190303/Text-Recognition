from preprocessing import preprocess_image
from inference import recognize_text
from utils import save_results, load_image_path

def main():
    print("Running OCR pipeline...")

    # Example directory containing images
    image_folder = "sample_images/"
    images = load_image_path(image_folder)

    for image_path in images:
        print(f"Processing: {image_path}")
        text = recognize_text(image_path)
        print(f"Recognized Text: {text}")

        # Save results
        save_results(text, "output.txt")

if __name__ == "__main__":
    main()
