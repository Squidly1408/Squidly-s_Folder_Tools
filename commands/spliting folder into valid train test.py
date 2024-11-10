import os
import random
import shutil
from pathlib import Path

def split_dataset(images_folder: str, output_folder: str):
    # Create the output directories
    train_folder = Path(output_folder) / 'train'
    test_folder = Path(output_folder) / 'test'
    val_folder = Path(output_folder) / 'val'
    
    train_folder.mkdir(parents=True, exist_ok=True)
    test_folder.mkdir(parents=True, exist_ok=True)
    val_folder.mkdir(parents=True, exist_ok=True)

    # Get all image files in the folder
    image_files = list(Path(images_folder).glob("*.[jJ][pP][gG]")) + \
                  list(Path(images_folder).glob("*.[pP][nN][gG]"))

    # Shuffle the list of files
    random.shuffle(image_files)

    # Split the files into 70% train, 15% test, 15% validation
    total_images = len(image_files)
    train_count = int(total_images * 0.7)
    test_count = int(total_images * 0.15)

    # Train files
    train_files = image_files[:train_count]
    # Test files
    test_files = image_files[train_count:train_count + test_count]
    # Validation files
    val_files = image_files[train_count + test_count:]

    # Move files to respective folders
    for img_file in train_files:
        shutil.copy(img_file, train_folder / img_file.name)
        # Copy the corresponding text file if it exists
        txt_file = img_file.with_suffix('.txt')
        if txt_file.exists():
            shutil.copy(txt_file, train_folder / txt_file.name)

    for img_file in test_files:
        shutil.copy(img_file, test_folder / img_file.name)
        txt_file = img_file.with_suffix('.txt')
        if txt_file.exists():
            shutil.copy(txt_file, test_folder / txt_file.name)

    for img_file in val_files:
        shutil.copy(img_file, val_folder / img_file.name)
        txt_file = img_file.with_suffix('.txt')
        if txt_file.exists():
            shutil.copy(txt_file, val_folder / txt_file.name)

    print(f"Dataset split completed:\n- Train: {len(train_files)} files\n- Test: {len(test_files)} files\n- Validation: {len(val_files)} files")

# Usage
if __name__ == "__main__":
    images_folder = 'path/to/your/images/folder'  # Update with your images folder
    output_folder = 'path/to/output/folder'  # Update with your desired output folder
    split_dataset(images_folder, output_folder)
