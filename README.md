**Image Resizer Tool**
-------------------

**Description:**
A simple Python-based image resizer tool that scans a folder of images and resizes them to a fixed dimension (300x300 pixels). It supports various image formats and saves the resized output to a separate folder. Useful for quick batch resizing tasks during development or web optimization.

**Features:**
- Automatically detects and resizes all images in the input folder.
- Supports popular image formats: .jpg, .jpeg, .png, .bmp, and .gif.
- Saves resized images to a new output directory.
- Skips and logs any corrupted or unsupported image files.
- Prints progress for each image processed.
- Empty folder handled

**Functions:**
- Reads all files from the images/ folder that match supported image formats.
- Resizes each image to 300x300 using PIL (Python Imaging Library).
- Saves the resized images to a folder named resized_images/.
- Prints success messages for each image and error messages if any fail.

**Tools used:**
- Python 3 – Main programming language.
- Pillow (PIL) – Python Imaging Library for image processing.
- os – Built-in module to handle folder creation, file paths, and directory listing.
- VS Code – Used to write and manage the project.

