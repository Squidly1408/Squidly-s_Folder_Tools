import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def resize_image():
    """Resize an image based on user input for width or height."""
    def perform_resize():
        try:
            width = int(width_entry.get())
            height = int(height_entry.get())
            if width <= 0 and height <= 0:
                messagebox.showerror("Error", "Width or Height must be greater than 0.")
                return

            # Load the image
            file_path = filedialog.askopenfilename(title="Select an image", 
                                                   filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
            if not file_path:
                return  # User cancelled the dialog

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
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                       filetypes=[("PNG files", "*.png"),
                                                                  ("JPEG files", "*.jpg"),
                                                                  ("All files", "*.*")])
            if save_path:
                img.save(save_path)
                messagebox.showinfo("Success", f"Image resized and saved to {save_path}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Create a simple GUI for input
    resize_window = tk.Toplevel()
    resize_window.title("Resize Image")
    
    tk.Label(resize_window, text="Width (0 to keep aspect ratio):").pack(pady=5)
    width_entry = tk.Entry(resize_window)
    width_entry.pack(pady=5)

    tk.Label(resize_window, text="Height (0 to keep aspect ratio):").pack(pady=5)
    height_entry = tk.Entry(resize_window)
    height_entry.pack(pady=5)

    tk.Button(resize_window, text="Resize", command=perform_resize).pack(pady=20)

if __name__ == "__main__":
    resize_image()
