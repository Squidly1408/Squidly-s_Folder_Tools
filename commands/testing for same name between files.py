import os
import sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def check_and_delete_files(target_folder, required_count, progress_bar):
    """Check for files with the same name and delete those that don't meet the count requirement."""
    # Dictionary to store file names without extensions
    file_count = {}

    # Iterate through files in the target folder
    for file in os.listdir(target_folder):
        # Get the file name without extension
        file_name = Path(file).stem
        # Count occurrences of each file name
        if file_name in file_count:
            file_count[file_name].append(file)
        else:
            file_count[file_name] = [file]

    # List to store files to delete
    files_to_delete = []

    # Check counts and prepare deletion list
    for files in file_count.values():
        if len(files) < required_count:
            files_to_delete.extend(files)

    # Total files to delete for progress calculation
    total_files = len(files_to_delete)
    
    # If there are no files to delete, show a message and return
    if total_files == 0:
        messagebox.showinfo("Info", "No files to delete.")
        return

    # Initialize the progress bar
    progress_bar['maximum'] = total_files
    progress_bar['value'] = 0

    # Delete files that don't meet the count requirement
    for file in files_to_delete:
        file_path = Path(target_folder) / file
        try:
            file_path.unlink()  # Delete the file
            progress_bar['value'] += 1  # Update the progress bar
            progress_bar.update()  # Force the GUI to update
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

    # Show completion message
    messagebox.showinfo("Completed", f"Deleted {total_files} files.")

def select_folder():
    """Open a dialog to select a folder."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_selected = filedialog.askdirectory()  # Show a dialog to select a folder
    root.destroy()  # Close the Tkinter window
    return folder_selected

def run_deletion_process():
    """Run the file deletion process with a progress bar."""
    required_count = 2  # You can modify this value if needed

    # Let user select the folder
    target_folder = select_folder()
    if not target_folder:
        print("No folder selected. Exiting.")
        return

    # Create a new Tkinter window for the progress bar
    progress_window = tk.Tk()
    progress_window.title("Deleting Files")
    progress_window.geometry('300x100')

    # Create and configure the progress bar
    progress_bar = ttk.Progressbar(progress_window, orient='horizontal', mode='determinate', length=250)
    progress_bar.pack(pady=20)

    # Run the file deletion process
    check_and_delete_files(target_folder, required_count, progress_bar)

    # Close the progress window
    progress_window.destroy()

if __name__ == "__main__":
    run_deletion_process()
