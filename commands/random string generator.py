import tkinter as tk
from tkinter import ttk
import random
import string


class RandomStringGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random String Generator")
        self.root.geometry("450x400")
        self.root.configure(bg="#2c3e50")

        # Title Label
        self.title_label = tk.Label(
            root,
            text="Random String Generator",
            bg="#34495e",
            fg="white",
            font=("Arial", 18, "bold"),
            padx=10,
            pady=10,
        )
        self.title_label.pack(fill="x", pady=10)

        # Length Input Frame
        self.length_frame = tk.Frame(root, bg="#2c3e50")
        self.length_frame.pack(pady=10)

        self.length_label = tk.Label(
            self.length_frame,
            text="Length:",
            bg="#2c3e50",
            fg="white",
            font=("Arial", 12),
        )
        self.length_label.pack(side="left", padx=10)

        self.length_var = tk.StringVar(value="8")
        self.length_entry = ttk.Entry(
            self.length_frame,
            textvariable=self.length_var,
            font=("Arial", 12),
            width=5,
        )
        self.length_entry.pack(side="left", padx=10)

        # Checkboxes Frame
        self.checkboxes_frame = tk.Frame(root, bg="#2c3e50")
        self.checkboxes_frame.pack(pady=10)

        self.include_numbers = tk.BooleanVar(value=True)
        self.include_special_chars = tk.BooleanVar(value=False)

        self.numbers_checkbox = ttk.Checkbutton(
            self.checkboxes_frame,
            text="Include Numbers",
            variable=self.include_numbers,
            style="TCheckbutton",
        )
        self.numbers_checkbox.pack(anchor="w", pady=5)

        self.special_chars_checkbox = ttk.Checkbutton(
            self.checkboxes_frame,
            text="Include Special Characters",
            variable=self.include_special_chars,
            style="TCheckbutton",
        )
        self.special_chars_checkbox.pack(anchor="w", pady=5)

        # Generate Button
        self.generate_button = ttk.Button(
            root,
            text="Generate",
            command=self.generate_random_string,
            style="Accent.TButton",
        )
        self.generate_button.pack(pady=20)

        # Output Frame
        self.output_frame = tk.Frame(root, bg="#2c3e50")
        self.output_frame.pack(pady=10)

        self.output_label = tk.Label(
            self.output_frame,
            text="Random String:",
            bg="#2c3e50",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        self.output_label.pack(side="left", padx=10)

        self.output_string = tk.StringVar(value="")
        self.output_entry = ttk.Entry(
            self.output_frame,
            textvariable=self.output_string,
            font=("Arial", 12),
            state="readonly",
            width=30,
        )
        self.output_entry.pack(side="left", padx=10)

        # Copy Button
        self.copy_button = ttk.Button(
            root,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard,
        )
        self.copy_button.pack(pady=20)

    def generate_random_string(self):
        """Generate and display a random string."""
        try:
            length = int(self.length_var.get())
            if length < 1:
                raise ValueError("Length must be at least 1.")

            # Define character set
            char_set = string.ascii_letters
            if self.include_numbers.get():
                char_set += string.digits
            if self.include_special_chars.get():
                char_set += string.punctuation

            if not char_set:
                raise ValueError(
                    "Character set cannot be empty. Enable at least one option."
                )

            random_string = "".join(random.choices(char_set, k=length))
            self.output_string.set(random_string)
        except ValueError as e:
            self.output_string.set(str(e))

    def copy_to_clipboard(self):
        """Copy the generated string to the clipboard."""
        random_string = self.output_string.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(random_string)
        self.root.update()  # Update the clipboard contents
        self.copy_button.config(text="Copied!", state="disabled")
        self.root.after(2000, self.reset_copy_button)

    def reset_copy_button(self):
        """Reset the copy button text and state."""
        self.copy_button.config(text="Copy to Clipboard", state="normal")


def run():
    root = tk.Tk()

    # Styling
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure(
        "TCheckbutton",
        background="#2c3e50",
        foreground="white",
        font=("Arial", 12),
    )
    style.configure(
        "Accent.TButton",
        background="#1abc9c",
        foreground="white",
        font=("Arial", 12, "bold"),
    )
    style.map(
        "Accent.TButton",
        background=[("active", "#16a085")],
        foreground=[("active", "white")],
    )

    app = RandomStringGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    run()
