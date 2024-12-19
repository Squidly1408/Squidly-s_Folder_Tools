# sections: folders

import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox


def rename_files(substring_to_remove, folder_path):
    # Convert folder_path to a Path object
    commands_path = Path(folder_path)

    # Iterate through all Python files in the selected folder
    renamed_files = []
    for file in commands_path.glob("*.py"):
        file_name = file.stem  # Get the file name without the extension
        # Find the index of the substring and truncate everything after it
        if substring_to_remove in file_name:
            new_file_name = file_name.split(substring_to_remove)[0]
            new_file_path = (
                commands_path / f"{new_file_name}.py"
            )  # Create new file path
            os.rename(file, new_file_path)  # Rename the file
            renamed_files.append((file.name, f"{new_file_name}.py"))

    return renamed_files


def select_folder():
    folder_path = filedialog.askdirectory(title="Select Folder")
    if folder_path:
        folder_label.config(text=f"Selected Folder: {folder_path}")
        rename_button.config(state="normal")
        return folder_path
    else:
        folder_label.config(text="No folder selected")
        rename_button.config(state="disabled")
        return None


def on_rename():
    substring = substring_entry.get()
    folder_path = folder_label.cget("text").replace("Selected Folder: ", "").strip()

    if not substring:
        messagebox.showerror("Error", "Please enter a substring to remove.")
        return

    renamed_files = rename_files(substring, folder_path)

    if renamed_files:
        messagebox.showinfo(
            "Renaming Complete",
            f"Renamed {len(renamed_files)} file(s):\n"
            + "\n".join(f"'{old}' → '{new}'" for old, new in renamed_files),
        )
    else:
        messagebox.showinfo("No Changes", "No files were renamed.")


# Create the UI
root = tk.Tk()
root.title("Python File Renamer")

# Input field for the substring
tk.Label(root, text="Enter Substring to Remove and Truncate After:").pack(pady=5)
substring_entry = tk.Entry(root, width=40)
substring_entry.pack(pady=5)

# Folder selection button
folder_label = tk.Label(root, text="No folder selected", fg="gray")
folder_label.pack(pady=5)

select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=5)

# Rename button
rename_button = tk.Button(
    root, text="Rename Files", command=on_rename, state="disabled"
)
rename_button.pack(pady=10)

# Run the application
root.mainloop()
