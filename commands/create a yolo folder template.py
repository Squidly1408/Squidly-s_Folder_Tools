# sections: folders, ai

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

# Set the template folder path
TEMPLATE_FOLDER = Path(__file__).parent / "yolo_training_folder_template_folder"


class CloneFolderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clone Folder Template")
        self.root.geometry("400x200")

        # Template Folder Label
        self.template_folder = TEMPLATE_FOLDER
        self.template_label = tk.Label(
            root, text=f"Template Folder: {self.template_folder}"
        )
        self.template_label.pack(pady=10)

        # Destination Folder Selection
        self.destination_folder = ""
        self.destination_label = tk.Label(root, text="Select Destination Folder:")
        self.destination_label.pack(pady=10)

        self.destination_button = tk.Button(
            root, text="Browse", command=self.select_destination
        )
        self.destination_button.pack(pady=5)

        # Clone Button
        self.clone_button = tk.Button(
            root, text="Clone Folder", command=self.clone_folder
        )
        self.clone_button.pack(pady=20)

    def select_destination(self):
        """Open a dialog to select the destination folder."""
        self.destination_folder = filedialog.askdirectory(
            title="Select Destination Folder"
        )
        if self.destination_folder:
            self.destination_label.config(
                text=f"Destination Folder: {self.destination_folder}"
            )

    def clone_folder(self):
        """Clone the selected template folder to the destination."""
        if not self.destination_folder:
            messagebox.showerror("Error", "Please select a destination folder.")
            return

        try:
            # Get the template folder name
            folder_name = os.path.basename(self.template_folder)
            # Create the destination path
            destination_path = os.path.join(self.destination_folder, folder_name)

            # Copy the template folder to the destination
            shutil.copytree(self.template_folder, destination_path)
            messagebox.showinfo("Success", f"Folder cloned to: {destination_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clone folder: {e}")


def run_clone_folder_gui():
    root = tk.Tk()
    app = CloneFolderApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_clone_folder_gui()
