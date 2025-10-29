
import os
from PIL import Image

# # Paths
tiff_folder = "D://Datasets//WHU - Tiles//test//label"  # Replace with the folder containing your TIFF images
jpg_folder = "D://Datasets//WHU - Tiles//test//label_jpg"    # Replace with the folder to save PNG images

# Create the destination folder if it doesn't exist
# os.makedirs(png_folder, exist_ok=True)

# # Convert TIFF images to PNG
# for file_name in os.listdir(tiff_folder):
#     if file_name.endswith('.tiff') or file_name.endswith('.tif'):  # Check for TIFF files
#         tiff_path = os.path.join(tiff_folder, file_name)
#         png_name = os.path.splitext(file_name)[0] + '.png'  # Change the file extension to .png
#         png_path = os.path.join(png_folder, png_name)

#         # Open the TIFF image and save it as PNG
#         try:
#             with Image.open(tiff_path) as img:
#                 img.save(png_path, 'PNG')
#             print(f"Converted: {file_name} to {png_name}")
#         except Exception as e:
#             print(f"Failed to convert {file_name}: {e}")

# print("All eligible TIFF images have been converted to PNG and saved in the specified folder!")



# # Paths
# # tiff_folder = "path_to_your_tiff_folder"  # Replace with the folder containing your TIFF images
# # jpg_folder = "path_to_your_jpg_folder"    # Replace with the folder to save JPG images

# # Create the destination folder if it doesn't exist
# os.makedirs(jpg_folder, exist_ok=True)

# Convert TIFF images to JPG
for file_name in os.listdir(tiff_folder):
    if file_name.endswith('.tiff') or file_name.endswith('.tif'):  # Check for TIFF files
        tiff_path = os.path.join(tiff_folder, file_name)
        jpg_name = os.path.splitext(file_name)[0] + '.jpg'  # Change the file extension to .jpg
        jpg_path = os.path.join(jpg_folder, jpg_name)

        # Open the TIFF image and save it as JPG
        try:
            with Image.open(tiff_path) as img:
                rgb_img = img.convert("RGB")  # Ensure the image is in RGB mode for JPG
                rgb_img.save(jpg_path, 'JPEG')
            print(f"Converted: {file_name} to {jpg_name}")
        except Exception as e:
            print(f"Failed to convert {file_name}: {e}")

print("All eligible TIFF images have been converted to JPG and saved in the specified folder!")







##################### convert to binary

# import os
# from PIL import Image

# # Paths
# input_folder = "D://Datasets//WHU - Tiles//test//label_jpg"  # Replace with the folder containing the images
# output_folder = "D://Datasets//WHU - Tiles//test//label_jpg_binary"  # Replace with the folder to save binary images

# # Create the output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# # Convert images to binary
# for file_name in os.listdir(input_folder):
#     input_path = os.path.join(input_folder, file_name)
#     output_path = os.path.join(output_folder, file_name)

#     # Check if the file is an image
#     if os.path.isfile(input_path):
#         try:
#             with Image.open(input_path) as img:
#                 # Convert image to binary (1-bit pixels, black and white)
#                 binary_image = img.convert("1")
#                 # Save the binary image
#                 binary_image.save(output_path)
#                 print(f"Converted {file_name} to binary format.")
#         except Exception as e:
#             print(f"Failed to process {file_name}: {e}")

# print("All images have been successfully converted to binary format!")


