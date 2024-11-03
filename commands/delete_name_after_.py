import os
from pathlib import Path

def rename_files(substring_to_remove):
    # Path to the commands folder
    commands_path = Path(__file__).parent

    # Iterate through all Python files in the commands folder
    for file in commands_path.glob("*.py"):
        # Get the file name without the extension
        file_name = file.stem
        # Create a new name by removing the specified substring
        new_file_name = file_name.replace(substring_to_remove, "")
        # Only rename if the new file name is different
        if new_file_name != file_name:
            # Create a new path for the renamed file
            new_file_path = commands_path / f"{new_file_name}.py"
            # Rename the file
            os.rename(file, new_file_path)
            print(f"Renamed: '{file.name}' to '{new_file_name}.py'")

if __name__ == "__main__":
    # Example: remove a substring from filenames
    substring = input("Enter the substring to remove from filenames: ")
    rename_files(substring)
