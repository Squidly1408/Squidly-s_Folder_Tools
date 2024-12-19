# sections: folders, ai

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import json
import requests
import shutil
from pathlib import Path

# Define the path where datasets will be temporarily stored
DATASETS_PATH = Path(__file__).parent / "datasets"

# COCO dataset links
COCO_DATASET_URL = "http://images.cocodataset.org/zips/train2017.zip"
COCO_ANNOTATIONS_URL = (
    "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
)

# COCO classes (placeholder; should correspond to actual class names in COCO)
COCO_CLASSES = [
    "person",
    "bicycle",
    "car",
    "motorbike",
    "airplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
]

# Supported output formats
SUPPORTED_FORMATS = ["YOLOv7", "YOLOv8", "YOLOv7-tiny"]


class DatasetDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Dataset Filter & Download")
        self.root.geometry("400x600")

        # Create a canvas and a scrollbar
        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(
            root, orient="vertical", command=self.canvas.yview
        )
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack the canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Create a frame for class checkboxes
        self.class_frame = tk.LabelFrame(
            self.scrollable_frame, text="Select Classes", padx=10, pady=10
        )
        self.class_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create a list of BooleanVars for each class
        self.class_vars = {class_name: tk.BooleanVar() for class_name in COCO_CLASSES}

        # Populate the class frame with checkboxes
        for class_name, var in self.class_vars.items():
            chk = tk.Checkbutton(self.class_frame, text=class_name, variable=var)
            chk.pack(anchor=tk.W)

        # Create a dropdown for dataset format
        self.format_var = tk.StringVar()
        self.format_var.set(SUPPORTED_FORMATS[0])  # Default value

        format_label = tk.Label(self.scrollable_frame, text="Select Format")
        format_label.pack(pady=5)

        self.format_dropdown = ttk.Combobox(
            self.scrollable_frame,
            textvariable=self.format_var,
            values=SUPPORTED_FORMATS,
            state="readonly",
        )
        self.format_dropdown.pack(pady=5)

        # Choose output location button
        self.save_location = tk.StringVar()
        save_button = tk.Button(
            self.scrollable_frame,
            text="Choose Save Location",
            command=self.choose_save_location,
        )
        save_button.pack(pady=10)

        # Display chosen save location
        self.save_location_label = tk.Label(
            self.scrollable_frame, text="No location chosen", fg="red"
        )
        self.save_location_label.pack()

        # Create progress bar
        self.progress_bar = ttk.Progressbar(
            self.scrollable_frame, orient="horizontal", length=300, mode="determinate"
        )
        self.progress_bar.pack(pady=10)

        # Download button
        download_button = tk.Button(
            self.scrollable_frame,
            text="Download Dataset",
            command=self.download_dataset,
        )
        download_button.pack(pady=20)

    def choose_save_location(self):
        """Open a file dialog to select the output folder."""
        folder = filedialog.askdirectory()
        if folder:
            self.save_location.set(folder)
            self.save_location_label.config(text=f"Save location: {folder}", fg="green")
        else:
            self.save_location_label.config(text="No location chosen", fg="red")

    def download_dataset(self):
        selected_classes = [
            class_name for class_name, var in self.class_vars.items() if var.get()
        ]
        selected_format = self.format_var.get()
        save_location = self.save_location.get()

        if not selected_classes:
            messagebox.showwarning(
                "No Classes Selected", "Please select at least one class."
            )
            return

        if not save_location:
            messagebox.showwarning("No Save Location", "Please choose a save location.")
            return

        messagebox.showinfo(
            "Downloading",
            f"Downloading and processing dataset for classes: {', '.join(selected_classes)} in format {selected_format}",
        )

        self.progress_bar["value"] = 0
        self.root.update_idletasks()

        # Step 1: Download dataset and annotations
        dataset_zip_path = DATASETS_PATH / "train2017.zip"
        annotations_zip_path = DATASETS_PATH / "annotations_trainval2017.zip"

        self.progress_bar["maximum"] = 100

        # Download dataset if not already present
        if not dataset_zip_path.exists():
            self.progress_bar["value"] += 10
            self.root.update_idletasks()
            self.download_file(COCO_DATASET_URL, dataset_zip_path)

        # Download annotations if not already present
        if not annotations_zip_path.exists():
            self.progress_bar["value"] += 20
            self.root.update_idletasks()
            self.download_file(COCO_ANNOTATIONS_URL, annotations_zip_path)

        # Step 2: Extract datasets
        self.progress_bar["value"] += 30
        self.root.update_idletasks()

        self.extract_zip(dataset_zip_path, DATASETS_PATH / "images")
        self.extract_zip(annotations_zip_path, DATASETS_PATH / "annotations")

        # Step 3: Load and filter annotations
        self.progress_bar["value"] += 40
        self.root.update_idletasks()

        filtered_annotations = self.filter_annotations(selected_classes)

        # Step 4: Save the filtered dataset
        self.save_filtered_dataset(
            filtered_annotations,
            selected_classes,
            Path(save_location) / selected_format,
        )

        self.progress_bar["value"] = 100
        self.root.update_idletasks()

        messagebox.showinfo(
            "Completed",
            f"Dataset prepared successfully in format: {selected_format} at {save_location}",
        )

    def download_file(self, url, destination):
        """Download a file from a URL to the destination."""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Raise an error for bad responses
            total_length = int(response.headers.get("content-length", 0))

            with open(destination, "wb") as f:
                if total_length == 0:
                    f.write(response.content)
                else:
                    dl = 0
                    for data in response.iter_content(chunk_size=4096):
                        dl += len(data)
                        f.write(data)
                        self.progress_bar["value"] = (dl / total_length) * 100
                        self.root.update_idletasks()

        except requests.exceptions.RequestException as e:
            messagebox.showerror(
                "Download Error", f"An error occurred during download: {e}"
            )

    def extract_zip(self, zip_path, extract_to):
        """Extract a ZIP file."""
        shutil.unpack_archive(zip_path, extract_to)

    def filter_annotations(self, selected_classes):
        """Filter COCO annotations by selected classes."""
        annotations_path = DATASETS_PATH / "annotations" / "instances_train2017.json"
        with open(annotations_path) as f:
            coco_data = json.load(f)

        filtered_annotations = {"images": [], "annotations": [], "categories": []}

        class_ids = {
            category["id"]: category["name"]
            for category in coco_data["categories"]
            if category["name"] in selected_classes
        }

        # Filter images and annotations based on selected classes
        for annotation in coco_data["annotations"]:
            if annotation["category_id"] in class_ids:
                filtered_annotations["annotations"].append(annotation)

        filtered_annotations["categories"] = [
            cat for cat in coco_data["categories"] if cat["name"] in selected_classes
        ]
        image_ids = {ann["image_id"] for ann in filtered_annotations["annotations"]}

        # Filter images
        filtered_annotations["images"] = [
            img for img in coco_data["images"] if img["id"] in image_ids
        ]

        return filtered_annotations

    def save_filtered_dataset(self, annotations, selected_classes, output_path):
        """Save the filtered annotations and corresponding images to the chosen output path."""
        output_path.mkdir(parents=True, exist_ok=True)

        # Save filtered annotations (in COCO format)
        with open(output_path / "filtered_annotations.json", "w") as f:
            json.dump(annotations, f)

        # Copy relevant images to the output directory
        images_path = output_path / "images"
        images_path.mkdir(exist_ok=True)

        for image in annotations["images"]:
            image_file = DATASETS_PATH / "images" / image["file_name"]
            if image_file.exists():
                shutil.copy(image_file, images_path / image["file_name"])


if __name__ == "__main__":
    if not DATASETS_PATH.exists():
        DATASETS_PATH.mkdir()

    root = tk.Tk()
    downloader = DatasetDownloader(root)
    root.mainloop()
