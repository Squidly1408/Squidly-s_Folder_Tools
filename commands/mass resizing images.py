import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os


def mass_resize_images():
    """Resize all images in a selected folder based on user input for width or height."""

    def select_input_folder():
        """Select the folder containing images."""
        folder_path = filedialog.askdirectory(title="Select folder with images")
        if folder_path:
            input_folder_var.set(folder_path)

    def select_output_folder():
        """Select the output folder to save resized images."""
        folder_path = filedialog.askdirectory(title="Select output folder")
        if folder_path:
            output_folder_var.set(folder_path)

    def perform_mass_resize():
        """Resize images based on user input."""
        try:
            width = int(width_entry.get())
            height = int(height_entry.get())

            # Ensure at least one dimension is greater than zero
            if width <= 0 and height <= 0:
                messagebox.showerror("Error", "Width or Height must be greater than 0.")
                return

            # Get selected input and output folders
            input_folder = input_folder_var.get()
            output_folder = output_folder_var.get()

            # Check if folders are selected
            if not input_folder:
                messagebox.showerror(
                    "Error", "Please select an input folder with images."
                )
                return
            if not output_folder:
                messagebox.showerror("Error", "Please select an output folder.")
                return

            # Get all image files in the input folder
            image_files = [
                f
                for f in os.listdir(input_folder)
                if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif"))
            ]
            if not image_files:
                messagebox.showerror(
                    "Error", "No image files found in the selected folder."
                )
                return

            # Resize each image
            for image_file in image_files:
                image_path = os.path.join(input_folder, image_file)
                img = Image.open(image_path)
                original_size = img.size

                # Resize the image while maintaining aspect ratio
                if width > 0 and height == 0:
                    # Resize by width
                    ratio = width / original_size[0]
                    new_size = (width, int(original_size[1] * ratio))
                elif height > 0 and width == 0:
                    # Resize by height
                    ratio = height / original_size[1]
                    new_size = (int(original_size[0] * ratio), height)
                else:
                    new_size = (width, height)

                # Perform resizing
                img = img.resize(new_size, Image.ANTIALIAS)

                # Save the resized image to the output folder
                save_path = os.path.join(output_folder, image_file)
                img.save(save_path)

            messagebox.showinfo("Success", "All images resized successfully.")

        except ValueError:
            messagebox.showerror(
                "Error", "Please enter valid numerical values for width and height."
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Create the main window
    root = tk.Tk()
    root.title("Mass Image Resizer")

    # Input folder selection
    input_folder_var = tk.StringVar()
    tk.Label(root, text="Input Folder (Images):").pack(pady=5)
    input_folder_entry = tk.Entry(root, textvariable=input_folder_var, width=50)
    input_folder_entry.pack(pady=5)
    tk.Button(root, text="Select Folder", command=select_input_folder).pack(pady=5)

    # Output folder selection
    output_folder_var = tk.StringVar()
    tk.Label(root, text="Output Folder (Save Resized Images):").pack(pady=5)
    output_folder_entry = tk.Entry(root, textvariable=output_folder_var, width=50)
    output_folder_entry.pack(pady=5)
    tk.Button(root, text="Select Folder", command=select_output_folder).pack(pady=5)

    # Width and Height input
    tk.Label(root, text="Width (0 to keep aspect ratio):").pack(pady=5)
    width_entry = tk.Entry(root)
    width_entry.pack(pady=5)

    tk.Label(root, text="Height (0 to keep aspect ratio):").pack(pady=5)
    height_entry = tk.Entry(root)
    height_entry.pack(pady=5)

    # Resize Button
    tk.Button(root, text="Resize Images", command=perform_mass_resize).pack(pady=20)

    # Start the main event loop
    root.mainloop()


if __name__ == "__main__":
    mass_resize_images()
