# sections: folders, images

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os


def mass_resize_images():
    """Resize multiple images based on user input for width or height."""

    def perform_mass_resize():
        try:
            width = int(width_entry.get())
            height = int(height_entry.get())
            if width <= 0 and height <= 0:
                messagebox.showerror("Error", "Width or Height must be greater than 0.")
                return

            # Load multiple images
            file_paths = filedialog.askopenfilenames(
                title="Select images",
                filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")],
            )
            if not file_paths:
                return  # User cancelled the dialog

            for file_path in file_paths:
                img = Image.open(file_path)
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

                # Save the resized image
                save_path = filedialog.asksaveasfilename(
                    initialfile=os.path.basename(file_path),
                    defaultextension=".png",
                    filetypes=[
                        ("PNG files", "*.png"),
                        ("JPEG files", "*.jpg"),
                        ("All files", "*.*"),
                    ],
                )
                if save_path:
                    img.save(save_path)

            messagebox.showinfo("Success", "All images resized successfully.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Create a simple GUI for input
    mass_resize_window = tk.Toplevel()
    mass_resize_window.title("Mass Resize Images")

    tk.Label(mass_resize_window, text="Width (0 to keep aspect ratio):").pack(pady=5)
    width_entry = tk.Entry(mass_resize_window)
    width_entry.pack(pady=5)

    tk.Label(mass_resize_window, text="Height (0 to keep aspect ratio):").pack(pady=5)
    height_entry = tk.Entry(mass_resize_window)
    height_entry.pack(pady=5)

    tk.Button(
        mass_resize_window, text="Resize Images", command=perform_mass_resize
    ).pack(pady=20)


if __name__ == "__main__":
    mass_resize_images()
