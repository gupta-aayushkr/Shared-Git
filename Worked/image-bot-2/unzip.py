import os
import zipfile
import shutil

def unzip_and_merge(src_folder, dest_folder):
    # Ensure the destination folder exists
    os.makedirs(dest_folder, exist_ok=True)

    # Iterate over all files in the source folder
    for item in os.listdir(src_folder):
        if item.endswith('.zip'):
            zip_path = os.path.join(src_folder, item)
            
            # Create a temporary directory to extract the contents of the zip file
            temp_dir = os.path.join(src_folder, 'temp')
            os.makedirs(temp_dir, exist_ok=True)
            
            # Extract the zip file into the temporary directory
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
            
            # Move all contents from the temporary directory to the destination folder
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    
            # Remove the temporary directory
            shutil.rmtree(temp_dir)

# Define source and destination folders
source_folder = '/Users/aayushgupta/Desktop/image-bot/midjourney/4 Aug/All zip'
destination_folder = '/Users/aayushgupta/Desktop/image-bot/midjourney/4 Aug/unzipped'

# Call the function
unzip_and_merge(source_folder, destination_folder)
