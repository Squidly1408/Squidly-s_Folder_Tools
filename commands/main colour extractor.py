import tkinter as tk
from tkinter import filedialog, messagebox
from colorthief import ColorThief
from pathlib import Path

class ColorExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Color Extractor")
        self.root.geometry('500x400')
        self.root.configure(bg='#171717')

        self.image_path = None
        self.main_colors = []

        # Set the window icon
        self.root.iconbitmap('icon.ico')

        # Create a canvas and scrollbar to make the entire window scrollable
        self.canvas = tk.Canvas(self.root, bg='#171717')
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.root, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill='y')

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas to hold all widgets
        self.scrollable_frame = tk.Frame(self.canvas, bg='#171717')
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Configure the frame to resize with the window
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        """Create all the UI components."""
        self.title_label = tk.Label(self.scrollable_frame, text="Select an Image to Extract Colors", fg="white", bg="#171717", font=("Arial", 16))
        self.title_label.pack(pady=20)

        # Load Image Button
        self.load_button = tk.Button(self.scrollable_frame, text="Load Image", command=self.load_image, bg="white", fg="#171717", borderwidth=2, relief="groove")
        self.load_button.pack(pady=10)

        # Color Display
        self.color_frame = tk.Frame(self.scrollable_frame, bg="#171717")
        self.color_frame.pack(pady=10)

        # Save Colors Button
        self.save_button = tk.Button(self.scrollable_frame, text="Save Colors", command=self.save_colors, bg="white", fg="#171717", borderwidth=2, relief="groove")
        self.save_button.pack(pady=5)

    def load_image(self):
        """Open a dialog to load an image and extract the main colors."""
        self.image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        
        if self.image_path:
            self.extract_colors(self.image_path)

    def extract_colors(self, image_path):
        """Extract the main 6 colors from the image using ColorThief."""
        try:
            color_thief = ColorThief(image_path)
            # Get the dominant color
            self.main_colors = color_thief.get_palette(color_count=6)
            
            # Clear any previous color display
            for widget in self.color_frame.winfo_children():
                widget.destroy()

            # Display the main colors as colored blocks with copy icons
            for color in self.main_colors:
                hex_color = "#{:02x}{:02x}{:02x}".format(*color)
                color_block_frame = tk.Frame(self.color_frame, bg="#171717")
                color_block_frame.pack(pady=5, fill="x")

                # Color block label
                color_block = tk.Label(color_block_frame, bg=hex_color, width=20, height=2)
                color_block.pack(side=tk.LEFT, padx=10)

                # Copy icon (button)
                copy_button = tk.Button(color_block_frame, text="Copy", command=lambda c=hex_color: self.copy_single_color(c), bg="white", fg="#171717", borderwidth=2, relief="groove")
                copy_button.pack(side=tk.LEFT, padx=10)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract colors: {e}")

    def copy_single_color(self, color):
        """Copy a single color to the clipboard."""
        self.root.clipboard_clear()
        self.root.clipboard_append(color)
        messagebox.showinfo("Success", f"Color {color} copied to clipboard!")

    def save_colors(self):
        """Save the extracted colors to a text file."""
        if self.main_colors:
            save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if save_path:
                try:
                    with open(save_path, 'w') as file:
                        for color in self.main_colors:
                            file.write("#{0:02x}{1:02x}{2:02x}\n".format(*color))
                    messagebox.showinfo("Success", "Colors saved successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save colors: {e}")
        else:
            messagebox.showwarning("No Image", "Please load an image first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorExtractorApp(root)
    root.mainloop()
