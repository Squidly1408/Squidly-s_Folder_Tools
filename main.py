import os
import tkinter as tk
from tkinter import ttk
import subprocess
import sys
from pathlib import Path

# Path to commands folder
COMMANDS_PATH = Path(__file__).parent / "commands"

class SquidlyFolderTools:
    def __init__(self, root):
        self.root = root
        self.root.title("Squidly's Folder Tools")
        self.root.geometry('400x300')
        self.root.configure(bg='#171717')  # Set background color

        # Remove default window decoration (for custom title bar)
        self.root.overrideredirect(True)

        # Custom Title Bar
        self.create_custom_title_bar()

        # Create Search Box
        self.search_var = tk.StringVar()
        search_frame = tk.Frame(root, bg='#171717')
        search_frame.pack(pady=10, padx=10, anchor='w')

        self.search_entry = tk.Entry(search_frame, textvariable=self.search_var, bg='#171717', fg='white',
                                     borderwidth=0, insertbackground='white', font=("Arial", 12))
        self.search_entry.insert(0, "Search...")
        self.search_entry.bind("<FocusIn>", self.clear_placeholder)
        self.search_entry.bind("<FocusOut>", self.add_placeholder)
        self.search_entry.pack(fill="x", expand=True)

        # Create divider
        divider = tk.Frame(root, height=2, bg="gray")
        divider.pack(fill="x", padx=10, pady=10)

        # Command Listbox
        self.commands_listbox = tk.Listbox(root, bg='#171717', fg='white', selectbackground='#00796b',
                                           selectforeground='white', activestyle='none', highlightthickness=0,
                                           borderwidth=0, font=("Arial", 12))
        self.commands_listbox.pack(fill="both", expand=True, padx=10, pady=5)

        # Load Commands initially
        self.load_commands()

        # Bind events
        self.search_var.trace('w', self.update_list)
        self.commands_listbox.bind("<Double-1>", self.run_selected_command)

    def create_custom_title_bar(self):
        """Create a custom title bar with a close button."""
        title_bar = tk.Frame(self.root, bg='#00796b', relief='flat', height=30)
        title_bar.pack(fill="x", side="top")

        title_label = tk.Label(title_bar, text="Squidly’s Folder Tools", bg='#00796b', fg='white', font=("Arial", 12, "bold"))
        title_label.pack(side="left", padx=10)

        close_button = tk.Button(title_bar, text="X", command=self.root.destroy, bg='#00796b', fg='white',
                                 font=("Arial", 10, "bold"), borderwidth=0, highlightthickness=0)
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

    def clear_placeholder(self, event):
        """Clear the placeholder text in the search box."""
        if self.search_entry.get() == "Search...":
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg='white')

    def add_placeholder(self, event):
        """Add the placeholder text if the search box is empty."""
        if not self.search_entry.get():
            self.search_entry.insert(0, "Search...")
            self.search_entry.config(fg='grey')

    def load_commands(self):
        """Load commands from the 'commands' folder."""
        self.commands = []
        for command_file in COMMANDS_PATH.glob("*.py"):
            self.commands.append(command_file.stem)

        self.update_list()

    def update_list(self, *args):
        """Update the command list based on the search box input."""
        search_term = self.search_var.get().lower()
        if search_term == "search...":
            search_term = ""

        filtered_commands = [cmd for cmd in self.commands if search_term in cmd.lower()]

        self.commands_listbox.delete(0, tk.END)
        for cmd in filtered_commands:
            self.commands_listbox.insert(tk.END, cmd)

    def run_selected_command(self, event=None):
        """Execute the selected command."""
        selected_command = self.commands_listbox.get(tk.ACTIVE)
        if selected_command:
            command_path = COMMANDS_PATH / f"{selected_command}.py"
            subprocess.Popen([sys.executable, str(command_path)])

# Function to make sure the script runs with pythonw.exe without opening a terminal
def run_gui():
    root = tk.Tk()
    app = SquidlyFolderTools(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
