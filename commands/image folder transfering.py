# sections: folders, images

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from PIL import Image, ImageTk
import shutil

# Path to commands folder
COMMANDS_PATH = Path(__file__).parent / "commands"


class ImageSorter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Sorter")
        self.root.geometry("600x400")
        self.root.configure(bg="#171717")

        # UI Elements
        self.instructions = tk.Label(
            root, text="Select a folder with images:", bg="#171717", fg="white"
        )
        self.instructions.pack(pady=10)

        self.select_folder_btn = tk.Button(
            root,
            text="Choose Folder",
            command=self.select_folder,
            bg="white",
            fg="#171717",
        )
        self.select_folder_btn.pack(pady=10)

        self.num_folders_label = tk.Label(
            root, text="Enter the number of folders:", bg="#171717", fg="white"
        )
        self.num_folders_label.pack(pady=10)

        self.num_folders_entry = tk.Entry(root)
        self.num_folders_entry.pack(pady=10)

        self.create_folders_btn = tk.Button(
            root,
            text="Create Folders",
            command=self.create_folders,
            bg="white",
            fg="#171717",
        )
        self.create_folders_btn.pack(pady=10)

        self.folder_path = None
        self.images = []
        self.image_index = 0
        self.folders = []

    def select_folder(self):
        """Select the folder containing images."""
        self.folder_path = filedialog.askdirectory(title="Select Folder with Images")
        if not self.folder_path:
            messagebox.showerror("Error", "No folder selected.")
        else:
            messagebox.showinfo("Success", f"Selected folder: {self.folder_path}")

    def create_folders(self):
        """Create subfolders based on user input."""
        try:
            num_folders = int(self.num_folders_entry.get())
            if not self.folder_path:
                raise ValueError("No folder selected.")

            self.folders = [
                Path(self.folder_path) / f"Folder_{i+1}" for i in range(num_folders)
            ]
            for folder in self.folders:
                folder.mkdir(exist_ok=True)

            messagebox.showinfo("Success", f"Created {num_folders} folders.")
            self.load_images()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_images(self):
        """Load all images from the selected folder."""
        self.images = (
            list(Path(self.folder_path).glob("*.png"))
            + list(Path(self.folder_path).glob("*.jpg"))
            + list(Path(self.folder_path).glob("*.jpeg"))
        )

        if not self.images:
            messagebox.showerror("Error", "No images found in the folder.")
        else:
            self.display_sorting_ui()

    def display_sorting_ui(self):
        """Open the UI for sorting images."""
        self.root.destroy()  # Close the current window

        sorting_window = tk.Tk()
        sorting_window.title("Image Sorting")
        sorting_window.geometry("800x600")
        sorting_window.configure(bg="#171717")

        self.current_image_label = tk.Label(
            sorting_window, text="", bg="#171717", fg="white"
        )
        self.current_image_label.pack(pady=10)

        self.canvas = tk.Canvas(
            sorting_window, width=600, height=400, bg="#171717", highlightthickness=0
        )
        self.canvas.pack(pady=10)

        self.folder_buttons_frame = tk.Frame(sorting_window, bg="#171717")
        self.folder_buttons_frame.pack(pady=10)

        # Add folder buttons
        for folder in self.folders:
            btn = tk.Button(
                self.folder_buttons_frame,
                text=folder.name,
                command=lambda folder=folder: self.move_image(folder),
                bg="white",
                fg="#171717",
                width=15,
            )
            btn.pack(side=tk.LEFT, padx=5)

        self.next_image()

    def next_image(self):
        """Display the next image."""
        if self.image_index < len(self.images):
            image_path = self.images[self.image_index]
            self.current_image_label.config(text=f"Image: {image_path.name}")

            img = Image.open(image_path)
            img.thumbnail((600, 400))
            img_tk = ImageTk.PhotoImage(img)

            self.canvas.image = img_tk  # Keep a reference to avoid garbage collection
            self.canvas.create_image(300, 200, image=img_tk)
        else:
            messagebox.showinfo("Completed", "All images sorted!")
            exit()

    def move_image(self, folder):
        """Move the current image to the selected folder."""
        if self.image_index < len(self.images):
            image_path = self.images[self.image_index]
            shutil.move(str(image_path), str(folder / image_path.name))
            self.image_index += 1
            self.next_image()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSorter(root)
    root.mainloop()
