
import os
import random
import shutil


# Paths for the three input folders
folder1 = "D://Datasets//WHU - Tiles//train//A"  # Replace with the path to the first folder
folder2 = "D://Datasets//WHU - Tiles//train//B"  # Replace with the path to the second folder
folder3 = "D://Datasets//WHU - Tiles//train//label"  # Replace with the path to the third folder

# Paths for the three output folders
output_folder1 = "D://Datasets//WHU - Tiles//val//A"  # Replace with the path for the first output folder
output_folder2 = "D://Datasets//WHU - Tiles//val//B"  # Replace with the path for the second output folder
output_folder3 = "D://Datasets//WHU - Tiles//val//label"  # Replace with the path for the third output folder

# Create output folders if they don't exist
os.makedirs(output_folder1, exist_ok=True)
os.makedirs(output_folder2, exist_ok=True)
os.makedirs(output_folder3, exist_ok=True)

# Get a list of image names in folder1 (assuming all folders contain the same names)
image_names = [f for f in os.listdir(folder1) if os.path.isfile(os.path.join(folder1, f))]
print (image_names[0])

# Randomly select 504 image names
selected_images = random.sample(image_names, 504)

# Move selected images to the respective output folders
for image in selected_images:
    # Move from folder1 to output_folder1
    shutil.move(os.path.join(folder1, image), os.path.join(output_folder1, image))
    # Move from folder2 to output_folder2
    shutil.move(os.path.join(folder2, image), os.path.join(output_folder2, image))
    # Move from folder3 to output_folder3
    shutil.move(os.path.join(folder3, image), os.path.join(output_folder3, image))

print("504 images have been successfully moved from each folder to their respective output folders!")











# ########################  A  ###########################
# # Paths
# dataset_folder = "D://Datasets//WHU - Tiles//train//A"  # Replace with the path to your dataset folder
# val_folder = "D://Datasets//WHU - Tiles//val//A"          # Replace with the path where you want to save the selected images

# # Create the 'val' folder if it doesn't exist
# os.makedirs(val_folder, exist_ok=True)

# # Get a list of all image files in the dataset folder
# all_images = [f for f in os.listdir(dataset_folder) if os.path.isfile(os.path.join(dataset_folder, f))]

# # Randomly select 504 images
# selected_images = random.sample(all_images, 504)

# # Move selected images to the 'val' folder
# for image in selected_images:
#     source = os.path.join(dataset_folder, image)
#     destination = os.path.join(val_folder, image)
#     shutil.move(source, destination)

# print(f"504 images have been successfully moved to the 'val' folder!")



# #######################  B  #####################

# dataset_folder = "D://Datasets//WHU - Tiles//train//B"  # Replace with the path to your dataset folder
# val_folder = "D://Datasets//WHU - Tiles//val//B"          # Replace with the path where you want to save the selected images

# # Create the 'val' folder if it doesn't exist
# os.makedirs(val_folder, exist_ok=True)

# # Get a list of all image files in the dataset folder
# all_images = [f for f in os.listdir(dataset_folder) if os.path.isfile(os.path.join(dataset_folder, f))]

# # Randomly select 504 images
# selected_images = random.sample(all_images, 504)

# # Move selected images to the 'val' folder
# for image in selected_images:
#     source = os.path.join(dataset_folder, image)
#     destination = os.path.join(val_folder, image)
#     shutil.move(source, destination)

# print(f"504 images have been successfully moved to the 'val' folder!")



# ##################### label ############################

# dataset_folder = "D://Datasets//WHU - Tiles//train//label"  # Replace with the path to your dataset folder
# val_folder = "D://Datasets//WHU - Tiles//val//label"          # Replace with the path where you want to save the selected images

# # Create the 'val' folder if it doesn't exist
# os.makedirs(val_folder, exist_ok=True)

# # Get a list of all image files in the dataset folder
# all_images = [f for f in os.listdir(dataset_folder) if os.path.isfile(os.path.join(dataset_folder, f))]

# # Randomly select 504 images
# selected_images = random.sample(all_images, 504)

# # Move selected images to the 'val' folder
# for image in selected_images:
#     source = os.path.join(dataset_folder, image)
#     destination = os.path.join(val_folder, image)
#     shutil.move(source, destination)

# print(f"504 images have been successfully moved to the 'val' folder!")