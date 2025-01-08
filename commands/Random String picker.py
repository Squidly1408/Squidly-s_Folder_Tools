# sections: other

import tkinter as tk
from tkinter import ttk
import random


class RandomPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Picker")
        self.root.geometry("400x300")
        self.root.configure(bg="#171717")

        self.entries = []  # To store the input entries
        self.init_ui()

    def init_ui(self):
        # Title Label
        title_label = tk.Label(
            self.root,
            text="Random Picker",
            bg="#171717",
            fg="white",
            font=("Arial", 16, "bold"),
        )
        title_label.pack(pady=10)

        # Frame for Inputs
        self.input_frame = tk.Frame(self.root, bg="#171717")
        self.input_frame.pack(fill="both", expand=True, padx=10)

        # Add Input Button
        add_button = tk.Button(
            self.root,
            text="Add Input",
            command=self.add_input,
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            padx=10,
        )
        add_button.pack(pady=5)

        # Generate Button
        generate_button = tk.Button(
            self.root,
            text="Generate",
            command=self.generate_random,
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            padx=10,
        )
        generate_button.pack(pady=5)

        # Label for Result
        self.result_label = tk.Label(
            self.root,
            text="Result: ",
            bg="#171717",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        self.result_label.pack(pady=10)

        # Add initial inputs
        for _ in range(3):  # Prefilled with 3 inputs
            self.add_input()

    def add_input(self, value=""):
        """Add a new input row with an entry and a delete button."""
        row_frame = tk.Frame(self.input_frame, bg="#171717")
        row_frame.pack(fill="x", pady=2)

        entry = tk.Entry(
            row_frame,
            bg="#292929",
            fg="white",
            font=("Arial", 12),
            insertbackground="white",
            borderwidth=0,
        )
        entry.insert(0, str(value) if value else len(self.entries) + 1)
        entry.pack(side="left", fill="x", expand=True, padx=5)

        delete_button = tk.Button(
            row_frame,
            text="✖",
            command=lambda: self.remove_input(row_frame),
            bg="#ff4d4d",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            width=3,
        )
        delete_button.pack(side="right", padx=5)

        self.entries.append(entry)

    def remove_input(self, row_frame):
        """Remove an input row."""
        index = self.input_frame.winfo_children().index(row_frame)
        self.entries.pop(index)
        row_frame.destroy()

    def generate_random(self):
        """Generate a random name or number from the list."""
        values = [entry.get() for entry in self.entries if entry.get()]
        if values:
            result = random.choice(values)
            self.result_label.config(text=f"Result: {result}")
        else:
            self.result_label.config(text="Result: No inputs available!")


if __name__ == "__main__":
    root = tk.Tk()
    app = RandomPickerApp(root)
    root.mainloop()
