import os
from PIL import Image

def convert_images_to_8bit(input_folder, output_folder):
    # Make sure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Go through all files in input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Skip if not a file
        if not os.path.isfile(file_path):
            continue

        try:
            # Open image
            img = Image.open(file_path)

            # Convert to 8-bit RGB
            img = img.convert("RGB")

            # Save to output folder with same filename (as .jpg)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
            img.save(output_path, "JPEG")

            print(f"Converted and saved: {output_path}")

        except Exception as e:
            print(f"Skipping {filename}: {e}")

# Example usage:
input_folder = r"D:\Face_recognition_Project\Testing Faces"   # put your folder with original pics
output_folder = r"D:\Face_recognition_Project\converted_images"  # new folder for 8-bit pics

convert_images_to_8bit(input_folder, output_folder)
