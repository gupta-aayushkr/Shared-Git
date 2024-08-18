import os
import re
from collections import defaultdict

# Define the directory containing the images
source_directory = "set-1"
destination_directory = "images"

# Function to create a safe filename
def safe_filename(s):
    return re.sub(r'[^a-zA-Z0-9-]', '-', s).strip('-')

# Dictionary to keep track of counts for each category
category_counts = defaultdict(int)

# Get a list of all image files in the source directory
image_files = [f for f in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, f))]

for image in image_files:
    # Extract the category part of the image name
    match = re.search(r'_(\w+)_pfp_', image)
    if match:
        category = match.group(1).lower()
        
        # Increment the count for this category
        category_counts[category] += 1
        
        # Create the new image name
        new_image_name = f"{safe_filename(category)}-pfp-{category_counts[category]}.png"
        
        # Create the category directory if it doesn't exist
        category_directory = os.path.join(destination_directory, f"{safe_filename(category)}-pfp")
        if not os.path.exists(category_directory):
            os.makedirs(category_directory)
        
        # Move and rename the image
        source_path = os.path.join(source_directory, image)
        destination_path = os.path.join(category_directory, new_image_name)
        os.rename(source_path, destination_path)
        
        print(f"Renamed {image} to {new_image_name} and moved to {category_directory}")

print("Bulk renaming completed.")
