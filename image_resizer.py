# Task-7
# Image Resizer Tool
# Author: Bineesha K P
# Date: 03-07-2025

import os
from PIL import Image

input_folder = "images"            # Folder containing original images
output_folder = "resized_images"   # Folder to save resized images

new_size = (300, 300)
os.makedirs(output_folder, exist_ok=True)
supported_ext = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

image_files = [f for f in os.listdir(input_folder)
               if f.lower().endswith(supported_ext)]

# Check if image folder is empty
if not image_files:
    print("No images found!.")
    exit()
else:
    for filename in image_files:
        img_path = os.path.join(input_folder, filename)
        try:
            with Image.open(img_path) as img:
                resized_img = img.resize(new_size)
                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path)
                print(f" Resized and saved: {output_path}")
        except Exception as e:
            print(f"Error in processing {filename}: {e}")
print(" All images resized successfully.")
