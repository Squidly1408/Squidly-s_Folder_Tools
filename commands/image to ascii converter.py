import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
from PIL import Image, ImageEnhance


class ImageToAsciiConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to ASCII Converter")
        self.root.geometry("600x550")
        self.root.configure(bg="#171717")  # Match original theme

        self.ascii_chars = "@%#*+=-:. "
        self.image = None
        self.ascii_art = ""
        self.brightness_factor = 1.0
        self.invert_ascii = False

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        title_label = tk.Label(
            self.root,
            text="Image to ASCII Converter",
            bg="#00796b",
            fg="white",
            font=("Arial", 14, "bold"),
            pady=10,
        )
        title_label.pack(fill="x")

        # Load Image Button
        self.load_button = tk.Button(
            self.root,
            text="Load Image",
            bg="#00796b",
            fg="white",
            font=("Arial", 10),
            command=self.load_image,
        )
        self.load_button.pack(pady=10)

        # Brightness Slider
        self.brightness_label = tk.Label(
            self.root, text="Brightness", bg="#171717", fg="white", font=("Arial", 10)
        )
        self.brightness_label.pack(pady=5)

        self.brightness_slider = ttk.Scale(
            self.root,
            from_=0.5,
            to=2.0,
            value=1.0,
            orient="horizontal",
            command=self.update_brightness,
        )
        self.brightness_slider.pack(pady=5, fill="x", padx=20)

        # Width Slider
        self.width_label = tk.Label(
            self.root, text="ASCII Width", bg="#171717", fg="white", font=("Arial", 10)
        )
        self.width_label.pack(pady=5)

        self.width_slider = ttk.Scale(
            self.root,
            from_=10,
            to=200,
            value=100,
            orient="horizontal",
            command=self.update_ascii,
        )
        self.width_slider.pack(pady=5, fill="x", padx=20)

        # Invert Toggle
        self.invert_var = tk.BooleanVar(value=False)
        self.invert_toggle = tk.Checkbutton(
            self.root,
            text="Invert ASCII Art",
            variable=self.invert_var,
            bg="#171717",
            fg="white",
            font=("Arial", 10),
            selectcolor="#00796b",
            command=self.update_ascii,
        )
        self.invert_toggle.pack(pady=5)

        # ASCII Art Display
        self.ascii_display = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Courier", 8),
            bg="#1e1e1e",
            fg="white",
            height=20,
            width=70,
            borderwidth=0,
        )
        self.ascii_display.pack(pady=10, padx=10)

        # Save and Copy Buttons
        button_frame = tk.Frame(self.root, bg="#171717")
        button_frame.pack(pady=5)

        self.save_button = tk.Button(
            button_frame,
            text="Save as Text File",
            bg="#00796b",
            fg="white",
            font=("Arial", 10),
            command=self.save_ascii,
        )
        self.save_button.pack(side="left", padx=5)

        self.copy_button = tk.Button(
            button_frame,
            text="Copy to Clipboard",
            bg="#00796b",
            fg="white",
            font=("Arial", 10),
            command=self.copy_to_clipboard,
        )
        self.copy_button.pack(side="right", padx=5)

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        if file_path:
            self.image = Image.open(file_path)
            self.update_ascii()

    def update_brightness(self, value):
        self.brightness_factor = float(value)
        self.update_ascii()

    def convert_to_ascii(self, image, width):
        """Convert an image to ASCII art."""
        image = image.convert("L")  # Convert to grayscale
        aspect_ratio = image.height / image.width
        new_height = int(aspect_ratio * width * 0.55)
        image = image.resize((width, new_height))

        # Adjust brightness
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(self.brightness_factor)

        # Map pixels to ASCII characters
        ascii_chars = (
            self.ascii_chars if not self.invert_var.get() else self.ascii_chars[::-1]
        )
        pixels = image.getdata()
        ascii_image = [
            ascii_chars[pixel // (256 // len(ascii_chars))] for pixel in pixels
        ]
        ascii_lines = [
            "".join(ascii_image[index : index + width])
            for index in range(0, len(ascii_image), width)
        ]
        return "\n".join(ascii_lines)

    def update_ascii(self, event=None):
        if self.image:
            width = int(self.width_slider.get())
            self.ascii_art = self.convert_to_ascii(self.image, width)
            self.ascii_display.delete(1.0, tk.END)
            self.ascii_display.insert(tk.END, self.ascii_art)

    def save_ascii(self):
        if self.ascii_art:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            )
            if file_path:
                with open(file_path, "w") as file:
                    file.write(self.ascii_art)

    def copy_to_clipboard(self):
        if self.ascii_art:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.ascii_art)
            self.root.update()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToAsciiConverter(root)
    root.mainloop()
