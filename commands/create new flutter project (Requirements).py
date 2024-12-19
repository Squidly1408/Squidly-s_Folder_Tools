# sections: code

import os
import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox


def create_flutter_project():
    # Set the path for the new Flutter project
    project_directory = r"C:/Users/lucas/development/projects"

    # Prompt the user for the project name
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    project_name = simpledialog.askstring(
        "Project Name", "Enter the Flutter project name:"
    )

    if project_name:
        # Full path for the new project
        project_path = os.path.join(project_directory, project_name)

        try:
            flutter_path = r"C:/Users/lucas/development/SDKs/flutter/bin/flutter.bat"
            result = subprocess.run(
                [flutter_path, "create", project_path],
                check=True,
                capture_output=True,
                text=True,
            )
            # Show success message
            messagebox.showinfo(
                "Success",
                f"Flutter project '{project_name}' created successfully at {project_path}.",
            )
            print(
                f"Flutter project '{project_name}' created successfully at {project_path}."
            )
        except subprocess.CalledProcessError as e:
            # If the Flutter command fails, show an error message
            messagebox.showerror("Error", f"Error creating project: {e.stderr}")
            print(f"Error creating project: {e.stderr}")
        except Exception as e:
            # Catch any other exceptions and show an error message
            messagebox.showerror("Unexpected Error", f"Unexpected error: {str(e)}")
            print(f"Unexpected error: {str(e)}")
    else:
        print("Project name was not provided.")
        messagebox.showwarning("Input Error", "You must provide a project name.")


# If running this script directly, call the function
if __name__ == "__main__":
    create_flutter_project()
