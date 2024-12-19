# sections: folders, code

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import subprocess


class CreateRequirementsTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Requirements File")
        self.root.geometry("400x200")
        self.root.configure(bg="#171717")  # Set background color

        # Remove default window decoration (for custom title bar)
        self.root.overrideredirect(True)

        # Custom Title Bar
        self.create_custom_title_bar()

        # Create Main Frame
        main_frame = tk.Frame(root, bg="#171717")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create and pack button to select folder
        self.select_button = tk.Button(
            main_frame,
            text="Select Folder",
            command=self.select_folder,
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        self.select_button.pack(pady=20)

        # Label to display the selected folder
        self.folder_label = tk.Label(
            main_frame, text="", bg="#171717", fg="white", font=("Arial", 12)
        )
        self.folder_label.pack(pady=10)

    def create_custom_title_bar(self):
        """Create a custom title bar with a close button."""
        title_bar = tk.Frame(self.root, bg="#00796b", relief="flat", height=30)
        title_bar.pack(fill="x", side="top")

        title_label = tk.Label(
            title_bar,
            text="Create Requirements File",
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        title_label.pack(side="left", padx=10)

        close_button = tk.Button(
            title_bar,
            text="X",
            command=self.root.destroy,
            bg="#00796b",
            fg="white",
            font=("Arial", 10, "bold"),
            borderwidth=0,
            highlightthickness=0,
        )
        close_button.pack(side="right", padx=10)

        # Allow dragging the window
        title_bar.bind("<B1-Motion>", self.move_window)
        title_bar.bind("<ButtonPress-1>", self.get_mouse_position)

    def get_mouse_position(self, event):
        """Store the mouse position on the window."""
        self.mouse_x = event.x
        self.mouse_y = event.y

    def move_window(self, event):
        """Drag the window."""
        x = self.root.winfo_pointerx() - self.mouse_x
        y = self.root.winfo_pointery() - self.mouse_y
        self.root.geometry(f"+{x}+{y}")

    def select_folder(self):
        """Prompt the user to select a folder and create requirements file."""
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_label.config(text=folder_path)
            self.create_requirements_file(folder_path)

    def create_requirements_file(self, folder_path):
        """Create a requirements.txt file with package versions."""
        result = subprocess.run(
            ["pipreqs", folder_path, "--force"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode == 0:
            messagebox.showinfo("Success", "requirements.txt created successfully")
        else:
            messagebox.showerror(
                "Error",
                "Failed to create requirements.txt. Please ensure pipreqs is installed.",
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = CreateRequirementsTool(root)
    root.mainloop()
