# sections: images

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image


class CustomImageResizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Image Resizer")
        self.root.geometry("400x250")
        self.root.configure(bg="#171717")  # Consistent with main code
        self.root.overrideredirect(True)  # Remove default window decoration

        # Custom Title Bar
        self.create_custom_title_bar()

        # Main Frame
        self.main_frame = tk.Frame(root, bg="#171717")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Width Entry
        self.width_var = tk.StringVar()
        tk.Label(
            self.main_frame,
            text="Width (0 to keep aspect ratio):",
            bg="#171717",
            fg="white",
        ).pack(pady=5)
        self.width_entry = tk.Entry(
            self.main_frame, textvariable=self.width_var, bg="#1c1c1c", fg="white"
        )
        self.width_entry.pack(pady=5)

        # Height Entry
        self.height_var = tk.StringVar()
        tk.Label(
            self.main_frame,
            text="Height (0 to keep aspect ratio):",
            bg="#171717",
            fg="white",
        ).pack(pady=5)
        self.height_entry = tk.Entry(
            self.main_frame, textvariable=self.height_var, bg="#1c1c1c", fg="white"
        )
        self.height_entry.pack(pady=5)

        # Resize Button
        self.resize_button = tk.Button(
            self.main_frame,
            text="Resize",
            command=self.resize_image,
            bg="#00796b",
            fg="white",
        )
        self.resize_button.pack(pady=20)

    def create_custom_title_bar(self):
        """Create a custom title bar with a close button."""
        title_bar = tk.Frame(self.root, bg="#00796b", relief="flat", height=30)
        title_bar.pack(fill="x", side="top")

        title_label = tk.Label(
            title_bar,
            text="Custom Image Resizer",
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

    def resize_image(self):
        try:
            width = int(self.width_var.get())
            height = int(self.height_var.get())
            if width <= 0 and height <= 0:
                messagebox.showerror("Error", "Width or Height must be greater than 0.")
                return

            # Load the image
            file_path = filedialog.askopenfilename(
                title="Select an image",
                filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")],
            )
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
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[
                    ("PNG files", "*.png"),
                    ("JPEG files", "*.jpg"),
                    ("All files", "*.*"),
                ],
            )
            if save_path:
                img.save(save_path)
                messagebox.showinfo(
                    "Success", f"Image resized and saved to {save_path}"
                )

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = CustomImageResizer(root)
    root.mainloop()
