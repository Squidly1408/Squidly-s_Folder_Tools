# sections: folder

import os
import random
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path


class FileSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("File Selector")
        self.root.geometry("600x400")
        self.root.configure(bg="#171717")

        # Remove default window decoration (for custom title bar)
        self.root.overrideredirect(True)

        # Custom Title Bar
        self.create_custom_title_bar()

        # Main Frame
        main_frame = tk.Frame(root, bg="#171717")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Select Button
        select_button = tk.Button(
            main_frame,
            text="Select",
            command=self.select_path,
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
            borderwidth=0,
            highlightthickness=0,
        )
        select_button.pack(pady=10)

        # Treeview Scrollbar
        tree_scroll = tk.Scrollbar(main_frame)
        tree_scroll.pack(side="right", fill="y")

        # File Explorer Treeview
        self.file_tree = ttk.Treeview(
            main_frame,
            yscrollcommand=tree_scroll.set,
            columns=("name"),
            selectmode="extended",
            style="Custom.Treeview",
        )
        self.file_tree.heading("#0", text="Path", anchor="w")
        self.file_tree.heading("name", text="Name", anchor="w")
        self.file_tree.column("#0", anchor="w", width=400)
        self.file_tree.column("name", anchor="w", width=150)
        self.file_tree.pack(fill="both", expand=True, pady=10)

        tree_scroll.config(command=self.file_tree.yview)

        # Bind select event
        self.file_tree.tag_bind("unchecked", "<Double-1>", self.on_check)
        self.file_tree.tag_bind("checked", "<Double-1>", self.on_check)

        # Buttons Frame
        buttons_frame = tk.Frame(main_frame, bg="#171717")
        buttons_frame.pack(pady=10)

        # Random Select Button
        random_button = tk.Button(
            buttons_frame,
            text="Random Select",
            command=self.random_select,
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
            borderwidth=0,
            highlightthickness=0,
        )
        random_button.pack(side="left", padx=10)

        # Number of Files Entry
        self.num_files_entry = tk.Entry(buttons_frame, width=5)
        self.num_files_entry.pack(side="left", padx=10)

        # Corrupt Button
        corrupt_button = tk.Button(
            buttons_frame,
            text="Corrupt",
            command=self.corrupt_files,
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
            borderwidth=0,
            highlightthickness=0,
        )
        corrupt_button.pack(side="right", padx=10)

        # Dictionary to store file paths and their states
        self.file_states = {}

    def create_custom_title_bar(self):
        """Create a custom title bar with a close button."""
        title_bar = tk.Frame(self.root, bg="#00796b", relief="flat", height=30)
        title_bar.pack(fill="x", side="top")

        title_label = tk.Label(
            title_bar,
            text="File Selector",
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

    def select_path(self):
        """Open a file/folder selection dialog."""
        path = filedialog.askdirectory() or filedialog.askopenfilename()
        if path:
            self.file_tree.delete(*self.file_tree.get_children())
            self.display_files(Path(path))

    def display_files(self, path):
        """Display files and folders in the selected directory."""

        def insert_items(parent, p):
            for item in p.iterdir():
                iid = self.file_tree.insert(
                    parent,
                    "end",
                    text=str(item),
                    values=(item.name,),
                    tags=("unchecked",),
                )
                if item.is_dir():
                    insert_items(iid, item)

        insert_items("", path)

    def on_check(self, event):
        """Toggle the file state and update color."""
        item = self.file_tree.identify_row(event.y)
        if item:
            current_tag = self.file_tree.item(item, "tags")[0]
            new_tag = "checked" if current_tag == "unchecked" else "unchecked"
            self.file_tree.item(item, tags=(new_tag,))
            self.update_file_color(item, new_tag)

    def update_file_color(self, item, tag):
        """Update the color of the file name when checked/unchecked."""
        color = "red" if tag == "checked" else "white"
        self.file_tree.tag_configure(tag, foreground=color)

    def random_select(self):
        """Randomly select multiple files from the treeview."""
        all_items = self.get_all_items("")
        if all_items:
            try:
                num_files = int(self.num_files_entry.get())
            except ValueError:
                num_files = 1

            selected_items = random.sample(all_items, min(num_files, len(all_items)))
            for item in selected_items:
                self.file_tree.item(item, tags=("checked",))
                self.update_file_color(item, "checked")

    def get_all_items(self, parent):
        """Get all items recursively from the treeview."""
        items = []
        for item in self.file_tree.get_children(parent):
            items.append(item)
            items.extend(self.get_all_items(item))
        return items

    def corrupt_files(self):
        """Corrupt the selected files."""
        corrupted_files = []

        def corrupt_item(item):
            path = Path(self.file_tree.item(item, "text"))
            if "checked" in self.file_tree.item(item, "tags"):
                if path.is_file():
                    with open(path, "wb") as f:
                        f.write(os.urandom(os.path.getsize(path)))
                    corrupted_files.append(path.name)
            for child_item in self.file_tree.get_children(item):
                corrupt_item(child_item)

        for item in self.file_tree.get_children():
            corrupt_item(item)

        if corrupted_files:
            messagebox.showinfo(
                "Corrupt",
                f"The following files have been corrupted:\n\n"
                + "\n".join(corrupted_files),
            )
        else:
            messagebox.showinfo("Corrupt", "No files were selected for corruption.")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileSelector(root)
    root.mainloop()
