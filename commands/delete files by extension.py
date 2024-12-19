import os
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, filedialog


def delete_files_by_extension(directory, extension):
    """Delete all files with the given extension in the specified directory."""
    # Convert the selected directory to a Path object
    current_directory = Path(directory)

    # Ensure the directory exists
    if not current_directory.exists() or not current_directory.is_dir():
        messagebox.showerror("Error", f"Invalid directory: {directory}")
        return []

    # Find and delete files with the specified extension
    deleted_files = []
    for file in current_directory.glob(f"*{extension}"):
        try:
            os.remove(file)
            deleted_files.append(file.name)
        except Exception as e:
            print(f"Error deleting {file.name}: {e}")

    return deleted_files


def on_select_folder_button_click():
    """Handle the select folder button click event."""
    # Ask the user to select a folder
    folder_selected = filedialog.askdirectory(title="Select a Folder")

    if folder_selected:
        folder_label.config(text=f"Selected Folder: {folder_selected}")
        global selected_folder
        selected_folder = folder_selected
    else:
        messagebox.showerror(
            "Input Error", "No folder selected. Please select a folder."
        )


def on_delete_button_click():
    """Handle the delete button click event."""
    # Ensure a folder has been selected
    if not selected_folder:
        messagebox.showerror(
            "Input Error", "Please select a folder before deleting files."
        )
        return

    # Get user input from the entry field
    extension = extension_entry.get()

    # Ensure the extension starts with a dot
    if not extension.startswith("."):
        extension = "." + extension

    if not extension:
        messagebox.showerror("Input Error", "Please enter a file extension.")
        return

    # Delete files in the selected folder and show the result
    deleted_files = delete_files_by_extension(selected_folder, extension)

    if deleted_files:
        messagebox.showinfo("Success", f"Deleted files: {', '.join(deleted_files)}")
    else:
        messagebox.showinfo(
            "No Files Found", f"No files with extension '{extension}' found."
        )


# Create the main window
root = tk.Tk()
root.title("File Deletion by Extension")

# Create and pack widgets
instruction_label = tk.Label(
    root,
    text="Click 'Select Folder' to choose a folder, then enter the extension to delete files.",
)
instruction_label.pack(pady=10)

# Button to select a folder
select_folder_button = tk.Button(
    root, text="Select Folder", command=on_select_folder_button_click
)
select_folder_button.pack(pady=5)

# Label to show the selected folder
folder_label = tk.Label(root, text="No folder selected")
folder_label.pack(pady=5)

# File extension input field
extension_label = tk.Label(
    root, text="Enter the file extension to delete (e.g., .txt):"
)
extension_label.pack(pady=10)

extension_entry = tk.Entry(root, width=30)
extension_entry.pack(pady=5)

# Button to delete files
delete_button = tk.Button(root, text="Delete Files", command=on_delete_button_click)
delete_button.pack(pady=20)

# Global variable to hold the selected folder
selected_folder = None

# Run the GUI
root.mainloop()
