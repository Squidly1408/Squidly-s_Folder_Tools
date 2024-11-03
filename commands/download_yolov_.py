import os
import requests
import zipfile
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def download_yolo(version, destination):
    """Downloads the specified YOLO version and extracts it to the destination."""
    if version == "v7":
        url = "https://github.com/WongKinYiu/yolov7/archive/refs/heads/main.zip"
    elif version == "v8":
        url = "https://github.com/ultralytics/yolov8/archive/refs/heads/main.zip"
    else:
        raise ValueError("Unsupported YOLO version.")

    # Download the YOLO model
    response = requests.get(url)
    if response.status_code == 200:
        zip_file_path = os.path.join(destination, f"yolov{version}.zip")

        with open(zip_file_path, 'wb') as f:
            f.write(response.content)

        # Extract the downloaded zip file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(destination)

        # Remove the zip file after extraction
        os.remove(zip_file_path)
        messagebox.showinfo("Success", f"YOLOv{version} downloaded and extracted to {destination}")
    else:
        messagebox.showerror("Error", "Failed to download the specified YOLO version.")


def choose_destination():
    """Opens a file dialog to select the destination directory."""
    return filedialog.askdirectory(title="Select Destination Directory")


def create_download_interface():
    """Creates a simple GUI to select YOLO version and destination."""
    root = tk.Tk()
    root.title("Download YOLO")

    tk.Label(root, text="Choose YOLO version:").pack(pady=10)
    version_var = tk.StringVar(value="v7")
    tk.Radiobutton(root, text="YOLOv7", variable=version_var, value="v7").pack(anchor=tk.W)
    tk.Radiobutton(root, text="YOLOv8", variable=version_var, value="v8").pack(anchor=tk.W)

    tk.Button(root, text="Select Destination", command=lambda: destination_var.set(choose_destination())).pack(pady=10)

    destination_var = tk.StringVar(value="")
    tk.Entry(root, textvariable=destination_var, state='readonly').pack(pady=10)

    tk.Button(root, text="Download", command=lambda: download_yolo(version_var.get(), destination_var.get())).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    create_download_interface()
