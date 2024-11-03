import os
from pathlib import Path

def delete_files_by_extension(extension):
    """Delete all files with the given extension in the current directory."""
    # Get the current directory
    current_directory = Path(__file__).parent

    # Find and delete files with the specified extension
    deleted_files = []
    for file in current_directory.glob(f"*{extension}"):
        try:
            os.remove(file)
            deleted_files.append(file.name)
        except Exception as e:
            print(f"Error deleting {file.name}: {e}")

    if deleted_files:
        print(f"Deleted files: {', '.join(deleted_files)}")
    else:
        print(f"No files with extension '{extension}' found.")

if __name__ == "__main__":
    # Get user input for the file extension
    extension = input("Enter the file extension to delete (e.g., .txt): ")
    
    if not extension.startswith('.'):
        extension = '.' + extension  # Ensure it starts with a dot

    delete_files_by_extension(extension)
