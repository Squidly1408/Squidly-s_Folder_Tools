import tkinter as tk
import subprocess
import sys
from pathlib import Path

# Base directory of the commands
BASE_PATH = Path(__file__).parent
GIT_COMMANDS_PATH = BASE_PATH / "git_commands"

# Paths to the individual Git command scripts
SCRIPT_PATHS = {
    "Clone Repository": GIT_COMMANDS_PATH / "git clone repo.py",
    "Pull Repository": GIT_COMMANDS_PATH / "git pull repo.py",
    "Create Repository": GIT_COMMANDS_PATH / "git create repo.py",
    "commit Repository": GIT_COMMANDS_PATH / "git commit repo.py",
    "Init Repository": GIT_COMMANDS_PATH / "git init repo.py",
    "Push Repository": GIT_COMMANDS_PATH / "git push to remote.py",
    "Status check": GIT_COMMANDS_PATH / "git status check.py",
    "Install GIT": GIT_COMMANDS_PATH / "install git.py",
}


def launch_script(script_name):
    """Launch the selected script."""
    script_path = SCRIPT_PATHS.get(script_name)
    if script_path and script_path.exists():
        subprocess.Popen([sys.executable, str(script_path)])
    else:
        tk.messagebox.showerror("Error", f"Script '{script_name}' not found!")


# Main UI setup
root = tk.Tk()
root.title("Git Commands")
root.geometry("300x200")
root.configure(bg="#171717")

tk.Label(root, text="Select a Git Command:", bg="#171717", fg="white").pack(pady=20)

# Dropdown for selecting Git commands
command_var = tk.StringVar()
command_var.set("Clone Repository")  # Default selection
dropdown = tk.OptionMenu(root, command_var, *SCRIPT_PATHS.keys())
dropdown.configure(bg="white", fg="#171717")
dropdown.pack(pady=10)

# Button to execute the selected script
run_button = tk.Button(
    root,
    text="Run Command",
    command=lambda: launch_script(command_var.get()),
    bg="white",
    fg="#171717",
    borderwidth=2,
    relief="groove",
)
run_button.pack(pady=20)

root.mainloop()
