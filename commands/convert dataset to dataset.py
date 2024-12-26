# sections: ai, folders

import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import sys
from pathlib import Path

# Path to commands folder
COMMANDS_PATH = Path(__file__).parent / "commands"
IMAGES_PATH = Path(__file__).parent / "images"


def convert_dataset(input_file, output_file):
    """Convert a dataset from one format to another based on file extension."""
    try:
        # Determine input and output formats
        input_extension = Path(input_file).suffix.lower()
        output_extension = Path(output_file).suffix.lower()

        # Read the input file based on its format
        if input_extension == ".csv":
            data = pd.read_csv(input_file)
        elif input_extension == ".json":
            data = pd.read_json(input_file)
        elif input_extension == ".xlsx":
            data = pd.read_excel(input_file)
        elif input_extension == ".parquet":
            data = pd.read_parquet(input_file)
        else:
            print(f"Unsupported input format: {input_extension}")
            return

        # Write to the output file based on the specified format
        if output_extension == ".csv":
            data.to_csv(output_file, index=False)
        elif output_extension == ".json":
            data.to_json(output_file, orient="records", lines=True)
        elif output_extension == ".xlsx":
            data.to_excel(output_file, index=False)
        elif output_extension == ".parquet":
            data.to_parquet(output_file, index=False)
        else:
            print(f"Unsupported output format: {output_extension}")
            return

        print(f"Successfully converted '{input_file}' to '{output_file}'.")
    except Exception as e:
        print(f"Error converting file: {e}")


class DatasetConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dataset Converter")
        self.root.geometry("400x250")
        self.root.configure(bg="#171717")

        self.create_widgets()

    def create_widgets(self):
        # Input File Selection
        self.input_label = tk.Label(
            self.root, text="Input File:", bg="#171717", fg="white", font=("Arial", 12)
        )
        self.input_label.pack(pady=5)
        self.input_entry = tk.Entry(
            self.root, bg="#333333", fg="white", font=("Arial", 12), width=50
        )
        self.input_entry.pack(pady=5)
        self.input_browse_btn = tk.Button(
            self.root,
            text="Browse",
            command=self.browse_input_file,
            bg="#00796b",
            fg="white",
            font=("Arial", 12),
        )
        self.input_browse_btn.pack(pady=5)

        # Output File Selection
        self.output_label = tk.Label(
            self.root, text="Output File:", bg="#171717", fg="white", font=("Arial", 12)
        )
        self.output_label.pack(pady=5)
        self.output_entry = tk.Entry(
            self.root, bg="#333333", fg="white", font=("Arial", 12), width=50
        )
        self.output_entry.pack(pady=5)
        self.output_browse_btn = tk.Button(
            self.root,
            text="Browse",
            command=self.browse_output_file,
            bg="#00796b",
            fg="white",
            font=("Arial", 12),
        )
        self.output_browse_btn.pack(pady=5)

        # Convert Button
        self.convert_btn = tk.Button(
            self.root,
            text="Convert",
            command=self.convert_dataset,
            bg="#00796b",
            fg="white",
            font=("Arial", 12),
        )
        self.convert_btn.pack(pady=20)

    def browse_input_file(self):
        input_file = filedialog.askopenfilename(
            title="Select Input File", filetypes=[("All Files", "*.*")]
        )
        if input_file:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, input_file)

    def browse_output_file(self):
        output_file = filedialog.asksaveasfilename(
            title="Select Output File",
            defaultextension=".csv",
            filetypes=[
                ("CSV Files", "*.csv"),
                ("JSON Files", "*.json"),
                ("Excel Files", "*.xlsx"),
                ("Parquet Files", "*.parquet"),
            ],
        )
        if output_file:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, output_file)

    def convert_dataset(self):
        input_file = self.input_entry.get()
        output_file = self.output_entry.get()

        if not input_file or not Path(input_file).is_file():
            messagebox.showerror("Error", "Please select a valid input file.")
            return

        if not output_file:
            messagebox.showerror("Error", "Please select a valid output file.")
            return

        try:
            convert_dataset(input_file, output_file)
            messagebox.showinfo(
                "Success", f"Successfully converted '{input_file}' to '{output_file}'."
            )
        except Exception as e:
            messagebox.showerror("Error", f"Error converting file: {e}")


def run_gui():
    root = tk.Tk()
    app = DatasetConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
