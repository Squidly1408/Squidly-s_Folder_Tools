import os
import random
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox


def split_dataset(images_folder: str, output_folder: str):
    # Create the output directories
    train_folder = Path(output_folder) / "train"
    test_folder = Path(output_folder) / "test"
    val_folder = Path(output_folder) / "val"

    train_folder.mkdir(parents=True, exist_ok=True)
    test_folder.mkdir(parents=True, exist_ok=True)
    val_folder.mkdir(parents=True, exist_ok=True)

    # Get all image files in the folder (jpg, png)
    image_files = (
        list(Path(images_folder).glob("*.jpg"))
        + list(Path(images_folder).glob("*.jpeg"))
        + list(Path(images_folder).glob("*.png"))
    )

    if not image_files:
        messagebox.showerror("Error", "No image files found in the selected folder.")
        return

    # Shuffle the list of files
    random.shuffle(image_files)

    # Split the files into 70% train, 15% test, 15% validation
    total_images = len(image_files)
    train_count = int(total_images * 0.7)
    test_count = int(total_images * 0.15)

    # Train files
    train_files = image_files[:train_count]
    # Test files
    test_files = image_files[train_count : train_count + test_count]
    # Validation files
    val_files = image_files[train_count + test_count :]

    # Move files to respective folders
    for img_file in train_files:
        shutil.copy(img_file, train_folder / img_file.name)
        # Copy the corresponding text file if it exists
        txt_file = img_file.with_suffix(".txt")
        if txt_file.exists():
            shutil.copy(txt_file, train_folder / txt_file.name)

    for img_file in test_files:
        shutil.copy(img_file, test_folder / img_file.name)
        txt_file = img_file.with_suffix(".txt")
        if txt_file.exists():
            shutil.copy(txt_file, test_folder / txt_file.name)

    for img_file in val_files:
        shutil.copy(img_file, val_folder / img_file.name)
        txt_file = img_file.with_suffix(".txt")
        if txt_file.exists():
            shutil.copy(txt_file, val_folder / txt_file.name)

    messagebox.showinfo(
        "Success",
        f"Dataset split completed:\n- Train: {len(train_files)} files\n- Test: {len(test_files)} files\n- Validation: {len(val_files)} files",
    )


def select_folder():
    folder_path = filedialog.askdirectory(title="Select Folder")
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)


def select_output_folder():
    output_folder_path = filedialog.askdirectory(title="Select Output Folder")
    if output_folder_path:
        output_folder_entry.delete(0, tk.END)
        output_folder_entry.insert(0, output_folder_path)


def run_split():
    images_folder = folder_entry.get()
    output_folder = output_folder_entry.get()

    if not images_folder or not output_folder:
        messagebox.showerror("Error", "Please select both input and output folders.")
        return

    split_dataset(images_folder, output_folder)


# Setting up the Tkinter UI
root = tk.Tk()
root.title("Dataset Splitter")

# Input Folder
folder_label = tk.Label(root, text="Select Image Folder:")
folder_label.pack(pady=5)

folder_entry = tk.Entry(root, width=50)
folder_entry.pack(padx=10, pady=5)

folder_button = tk.Button(root, text="Browse", command=select_folder)
folder_button.pack(pady=5)

# Output Folder
output_folder_label = tk.Label(root, text="Select Output Folder:")
output_folder_label.pack(pady=5)

output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.pack(padx=10, pady=5)

output_folder_button = tk.Button(root, text="Browse", command=select_output_folder)
output_folder_button.pack(pady=5)

# Run Button
run_button = tk.Button(root, text="Split Dataset", command=run_split)
run_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
