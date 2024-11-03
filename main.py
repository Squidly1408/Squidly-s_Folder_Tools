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

        # Set the window icon
        self.root.iconbitmap(Path(__file__).parent / 'icon.ico')
        

        # Create Search Box
        self.search_var = tk.StringVar()
        search_frame = tk.Frame(root, bg='#171717')
        search_frame.pack(pady=10)

        search_entry = tk.Entry(search_frame, textvariable=self.search_var, bg='#171717', fg='white', 
                                 borderwidth=2, relief="groove")
        search_entry.pack(side=tk.LEFT, padx=(0, 10))

        # Create Dropdown List for Commands
        self.commands_var = tk.StringVar()
        self.commands_dropdown = ttk.Combobox(search_frame, textvariable=self.commands_var, 
                                               background='#171717', foreground='white', state='readonly')
        self.commands_dropdown.pack(side=tk.LEFT)

        # Load Commands initially
        self.load_commands()

        # Bind search functionality
        self.search_var.trace('w', self.update_list)

        # Create Run Button
        run_button = tk.Button(root, text="Run Command", command=self.run_selected_command, 
                               bg='white', fg='#171717', borderwidth=2, relief="groove")
        run_button.pack(pady=20)

        # Add Search Update Event
        self.update_list()

    def load_commands(self):
        """Load commands from the 'commands' folder."""
        self.commands = []
        for command_file in COMMANDS_PATH.glob("*.py"):
            self.commands.append(command_file.stem)

        self.commands_dropdown['values'] = self.commands

    def update_list(self, *args):
        """Update the command list based on the search box input."""
        search_term = self.search_var.get().lower()
        filtered_commands = [cmd for cmd in self.commands if search_term in cmd.lower()]
        self.commands_dropdown['values'] = filtered_commands

        # Automatically select the first matched command
        if filtered_commands:
            self.commands_var.set(filtered_commands[0])
        else:
            self.commands_var.set("")

    def run_selected_command(self):
        """Execute the selected command."""
        selected_command = self.commands_var.get()
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
