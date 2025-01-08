# sections: images

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os


class ImagePixelationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixelation Tool")
        self.root.geometry("800x600")
        self.root.configure(bg="#171717")

        # Image variable to hold the loaded image
        self.image = None
        self.pixelated_image = None

        # Create Main Frame
        main_frame = tk.Frame(root, bg="#171717")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create Canvas for Image Display
        self.canvas = tk.Canvas(main_frame, bg="#171717", width=600, height=400)
        self.canvas.pack(padx=10, pady=10)

        # Create Pixelation Controls Frame
        controls_frame = tk.Frame(main_frame, bg="#171717")
        controls_frame.pack(pady=20)

        # Pick Image Button
        self.pick_button = tk.Button(
            controls_frame,
            text="Pick an Image",
            command=self.pick_image,
            bg="#00796b",
            fg="white",
            font=("Arial", 12),
            relief="flat",
        )
        self.pick_button.grid(row=0, column=0, padx=10)

        # Pixelation Level Text Input
        self.pixelation_label = tk.Label(
            controls_frame,
            text="Pixelation Level:",
            bg="#171717",
            fg="white",
            font=("Arial", 12),
        )
        self.pixelation_label.grid(row=0, column=1, padx=10)

        self.pixelation_entry = tk.Entry(
            controls_frame, font=("Arial", 12), bg="#444444", fg="white", width=5
        )
        self.pixelation_entry.insert(0, "10")  # Default pixelation level
        self.pixelation_entry.grid(row=0, column=2, padx=10)

        # Pixelate Button
        self.pixelate_button = tk.Button(
            controls_frame,
            text="Pixelate Image",
            command=self.pixelate_image,
            bg="#00796b",
            fg="white",
            font=("Arial", 12),
            relief="flat",
        )
        self.pixelate_button.grid(row=0, column=3, padx=10)

        # Save Image Button
        self.save_button = tk.Button(
            controls_frame,
            text="Save Image",
            command=self.save_image,
            bg="#00796b",
            fg="white",
            font=("Arial", 12),
            relief="flat",
        )
        self.save_button.grid(row=0, column=4, padx=10)

    def pick_image(self):
        """Open file explorer to pick an image."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)

    def pixelate_image(self):
        """Pixelate the image based on the user's chosen pixelation level."""
        if self.image:
            try:
                # Get the pixelation level from the text entry
                pixel_size = int(self.pixelation_entry.get())
                if pixel_size < 1:
                    raise ValueError("Pixelation level must be greater than 0.")

                # Resize the image to create the pixelated effect
                small = self.image.resize(
                    (self.image.width // pixel_size, self.image.height // pixel_size),
                    resample=Image.Resampling.NEAREST,
                )
                self.pixelated_image = small.resize(
                    self.image.size, Image.Resampling.NEAREST
                )

                # Display the pixelated image
                self.display_image(self.pixelated_image)
            except ValueError:
                messagebox.showerror(
                    "Invalid Input", "Please enter a valid pixelation level."
                )
        else:
            messagebox.showwarning("No Image", "Please pick an image first.")

    def display_image(self, img):
        """Display the given image on the canvas, scaled to fit the canvas."""
        img_width, img_height = img.size
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Scale the image to fit the canvas while maintaining aspect ratio
        if img_width > canvas_width or img_height > canvas_height:
            scale_factor = min(canvas_width / img_width, canvas_height / img_height)
            img = img.resize(
                (int(img_width * scale_factor), int(img_height * scale_factor)),
                resample=Image.Resampling.LANCZOS,
            )

        # Convert image to PhotoImage
        img_tk = ImageTk.PhotoImage(img)

        # Clear the canvas before displaying the new image
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=img_tk)
        self.canvas.image = img_tk  # Keep a reference to prevent garbage collection

    def save_image(self):
        """Save the pixelated image to a file."""
        if self.pixelated_image:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[
                    ("PNG Image", "*.png"),
                    ("JPEG Image", "*.jpg;*.jpeg"),
                    ("All Files", "*.*"),
                ],
                title="Save Pixelated Image",
            )
            if file_path:
                self.pixelated_image.save(file_path)
                messagebox.showinfo(
                    "Image Saved", f"Image saved as {os.path.basename(file_path)}"
                )
        else:
            messagebox.showwarning("No Image", "Please pixelate an image first.")


# Function to run the pixelation app
def run_pixelation_app():
    root = tk.Tk()
    app = ImagePixelationApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_pixelation_app()
