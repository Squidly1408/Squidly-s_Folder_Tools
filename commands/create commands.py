# sections: folders

import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, Text, Scrollbar, Frame
from pathlib import Path
import subprocess
import sys
import keyword
import re

# Path to commands folder
COMMANDS_PATH = Path(__file__).parent
IMAGES_PATH = Path(__file__).parent / "images"

# Define sections
SECTIONS = ["code", "folder", "images", "ai", "other"]


class CommandManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Command Manager")
        self.root.geometry("1000x600")
        self.root.configure(bg="#171717")

        # Remove default window decoration (for custom title bar)
        self.root.overrideredirect(True)

        # Custom Title Bar
        self.create_custom_title_bar()

        # Create Main Frame
        main_frame = tk.Frame(root, bg="#171717")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create Button Frame
        button_frame = tk.Frame(main_frame, bg="#171717")
        button_frame.pack(fill="x")

        # Create Buttons
        create_button = tk.Button(
            button_frame,
            text="Create Command",
            command=self.create_command,
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        create_button.pack(side="left", padx=5, pady=5)

        save_button = tk.Button(
            button_frame,
            text="Save Command",
            command=self.save_command,
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        save_button.pack(side="left", padx=5, pady=5)

        delete_button = tk.Button(
            button_frame,
            text="Delete Command",
            command=self.delete_command,
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        delete_button.pack(side="left", padx=5, pady=5)

        install_button = tk.Button(
            button_frame,
            text="Install Package",
            command=self.install_package,
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        install_button.pack(side="left", padx=5, pady=5)

        run_button = tk.Button(
            button_frame,
            text="Run Command",
            command=self.run_command,
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        run_button.pack(side="left", padx=5, pady=5)

        # Create Left Frame for Commands Listbox
        left_frame = tk.Frame(main_frame, bg="#171717")
        left_frame.pack(side="left", fill="y")

        # Create Right Frame for Text Editor and Terminal
        right_frame = tk.Frame(main_frame, bg="#171717")
        right_frame.pack(side="right", fill="both", expand=True)

        # Create Command Listbox
        self.command_listbox = tk.Listbox(
            left_frame,
            bg="#171717",
            fg="white",
            selectbackground="#00796b",
            selectforeground="white",
            font=("Arial", 12),
        )
        self.command_listbox.pack(fill="y", expand=True, padx=5, pady=5)
        self.command_listbox.bind("<<ListboxSelect>>", self.load_command_code)

        # Create Text Frame for Code Display
        text_frame = tk.Frame(right_frame, bg="#171717")
        text_frame.pack(fill="both", expand=True, pady=10)

        self.code_text = Text(
            text_frame,
            bg="#171717",
            fg="white",
            insertbackground="white",
            font=("Arial", 12),
        )
        self.code_text.pack(fill="both", expand=True, padx=5, pady=5)
        self.code_text.bind("<KeyRelease>", self.highlight_syntax)

        # Create Terminal Frame
        terminal_frame = tk.Frame(right_frame, bg="#171717")
        terminal_frame.pack(fill="x", expand=False, pady=10)

        self.terminal_text = Text(
            terminal_frame,
            bg="black",
            fg="white",
            insertbackground="white",
            font=("Courier", 12),
        )
        self.terminal_text.pack(fill="both", expand=True, padx=5, pady=5)

        self.current_command = None
        self.load_commands()

        # Configure tags for syntax highlighting
        self.code_text.tag_configure("keyword", foreground="orange")
        self.code_text.tag_configure("builtin", foreground="blue")
        self.code_text.tag_configure("string", foreground="green")
        self.code_text.tag_configure("comment", foreground="gray")
        self.code_text.tag_configure("number", foreground="purple")
        self.code_text.tag_configure("operator", foreground="red")
        self.code_text.tag_configure("function", foreground="cyan")

    def create_custom_title_bar(self):
        """Create a custom title bar with a close button."""
        title_bar = tk.Frame(self.root, bg="#00796b", relief="flat", height=30)
        title_bar.pack(fill="x", side="top")

        title_label = tk.Label(
            title_bar,
            text="Command Manager",
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

    def load_commands(self):
        self.command_listbox.delete(0, tk.END)
        for command_file in COMMANDS_PATH.glob("*.py"):
            self.command_listbox.insert(tk.END, command_file.stem)

    def create_command(self):
        title = simpledialog.askstring("Command Title", "Enter the command title:")
        if not title:
            return

        section = simpledialog.askstring(
            "Command Sections",
            f"Enter the sections (available: {', '.join(SECTIONS)}):",
        )
        if not section:
            return

        self.code_text.delete(1.0, tk.END)
        self.code_text.insert(tk.END, f"# sections: {section}\n")
        self.code_text.insert(tk.END, "# Write your command code here")
        self.current_command = title

    def save_command(self):
        if not self.current_command:
            messagebox.showwarning(
                "No Command", "No command is currently being worked on."
            )
            return

        command_path = COMMANDS_PATH / f"{self.current_command}.py"
        code = self.code_text.get(1.0, tk.END)

        with open(command_path, "w") as f:
            f.write(code.strip())

        self.load_commands()

    def delete_command(self):
        selected_command = self.command_listbox.get(tk.ACTIVE)
        if not selected_command:
            return

        command_path = COMMANDS_PATH / f"{selected_command}.py"
        os.remove(command_path)
        self.load_commands()
        self.code_text.delete(1.0, tk.END)

    def install_package(self):
        package_name = simpledialog.askstring(
            "Install Package", "Enter the package name to install:"
        )
        if package_name:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package_name]
            )
            messagebox.showinfo(
                "Installation", f"Package '{package_name}' installed successfully."
            )

    def run_command(self):
        if not self.current_command:
            messagebox.showwarning(
                "No Command", "No command is currently being worked on."
            )
            return

        command_path = COMMANDS_PATH / f"{self.current_command}.py"
        process = subprocess.Popen(
            [sys.executable, str(command_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = process.communicate()

        self.terminal_text.delete(1.0, tk.END)
        self.terminal_text.insert(tk.END, stdout.decode("utf-8"))
        if stderr:
            self.terminal_text.insert(tk.END, "\nErrors:\n")
            self.terminal_text.insert(tk.END, stderr.decode("utf-8"))

    def load_command_code(self, event):
        selected_command = self.command_listbox.get(tk.ACTIVE)
        if selected_command:
            self.current_command = selected_command
            command_path = COMMANDS_PATH / f"{selected_command}.py"
            with open(command_path, "r") as f:
                code = f.read()

            self.code_text.delete(1.0, tk.END)
            self.code_text.insert(tk.END, code)
            self.highlight_syntax()

    def highlight_syntax(self, event=None):
        # Reset all text to default color
        self.code_text.tag_remove("keyword", "1.0", tk.END)
        self.code_text.tag_remove("builtin", "1.0", tk.END)
        self.code_text.tag_remove("string", "1.0", tk.END)
        self.code_text.tag_remove("comment", "1.0", tk.END)
        self.code_text.tag_remove("number", "1.0", tk.END)
        self.code_text.tag_remove("operator", "1.0", tk.END)
        self.code_text.tag_remove("function", "1.0", tk.END)

        # Get all text
        content = self.code_text.get(1.0, tk.END)

        # Regular expressions for syntax highlighting
        keyword_pattern = r"\b(" + "|".join(keyword.kwlist) + r")\b"
        builtin_pattern = r"\b(" + "|".join(dir(__builtins__)) + r")\b"
        string_pattern = r"(\'[^\']*\'|\"[^\"]*\")"
        comment_pattern = r"#[^\n]*"
        number_pattern = r"\b\d+\b"
        operator_pattern = r"[\+\-\*\%\/=<>!]"
        function_pattern = r"\bdef\b\s+(\w+)"

        for match in re.finditer(keyword_pattern, content):
            start_index = self.code_text.index(f"1.0+{match.start()}c")
            end_index = self.code_text.index(f"1.0+{match.end()}c")
            self.code_text.tag_add("keyword", start_index, end_index)

        for match in re.finditer(builtin_pattern, content):
            start_index = self.code_text.index(f"1.0+{match.start()}c")
            end_index = self.code_text.index(f"1.0+{match.end()}c")
            self.code_text.tag_add("builtin", start_index, end_index)

        for match in re.finditer(string_pattern, content):
            start_index = self.code_text.index(f"1.0+{match.start()}c")
            end_index = self.code_text.index(f"1.0+{match.end()}c")
            self.code_text.tag_add("string", start_index, end_index)

        for match in re.finditer(comment_pattern, content):
            start_index = self.code_text.index(f"1.0+{match.start()}c")
            end_index = self.code_text.index(f"1.0+{match.end()}c")
            self.code_text.tag_add("comment", start_index, end_index)

        for match in re.finditer(number_pattern, content):
            start_index = self.code_text.index(f"1.0+{match.start()}c")
            end_index = self.code_text.index(f"1.0+{match.end()}c")
            self.code_text.tag_add("number", start_index, end_index)

        for match in re.finditer(operator_pattern, content):
            start_index = self.code_text.index(f"1.0+{match.start()}c")
            end_index = self.code_text.index(f"1.0+{match.end()}c")
            self.code_text.tag_add("operator", start_index, end_index)

        for match in re.finditer(function_pattern, content):
            start_index = self.code_text.index(f"1.0+{match.start(1)}c")
            end_index = self.code_text.index(f"1.0+{match.end(1)}c")
            self.code_text.tag_add("function", start_index, end_index)


def run_command_manager():
    root = tk.Tk()
    app = CommandManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_command_manager()
