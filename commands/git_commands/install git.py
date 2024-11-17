import tkinter as tk
from tkinter import ttk
import subprocess
import sys
import threading
import os
import platform


class GitInstallerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Git Installer")
        self.root.geometry("400x200")
        self.root.configure(bg="#171717")

        # Status Label
        self.status_label = tk.Label(
            self.root,
            text="Click 'Install Git' to begin.",
            bg="#171717",
            fg="white",
            font=("Arial", 12),
        )
        self.status_label.pack(pady=10)

        # Progress Bar
        self.progress_bar = ttk.Progressbar(
            self.root, orient="horizontal", length=300, mode="determinate"
        )
        self.progress_bar.pack(pady=20)

        # Install Button
        self.install_button = tk.Button(
            self.root,
            text="Install Git",
            command=self.start_installation,
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        self.install_button.pack(pady=10)

    def start_installation(self):
        self.install_button.config(
            state="disabled"
        )  # Disable the button during the process
        threading.Thread(target=self.download_and_install_git).start()

    def download_and_install_git(self):
        try:
            self.update_status("Downloading Git...")
            self.update_progress(20)

            if platform.system() == "Windows":
                installer_url = "https://github.com/git-for-windows/git/releases/download/v2.42.0.windows.1/Git-2.42.0-64-bit.exe"
                installer_path = os.path.join(os.getenv("TEMP"), "GitInstaller.exe")

                # Download the Git installer
                subprocess.run(
                    [sys.executable, "-m", "wget", installer_url, "-O", installer_path],
                    check=True,
                )

                self.update_status("Installing Git...")
                self.update_progress(60)

                # Run the Git installer silently
                subprocess.run([installer_path, "/SILENT"], check=True)

            elif platform.system() == "Linux":
                self.update_status("Installing Git via apt...")
                self.update_progress(40)

                # Install Git using the system package manager
                subprocess.run(["sudo", "apt-get", "update"], check=True)
                subprocess.run(["sudo", "apt-get", "install", "-y", "git"], check=True)

            elif platform.system() == "Darwin":  # macOS
                self.update_status("Installing Git via Homebrew...")
                self.update_progress(40)

                # Install Git using Homebrew
                subprocess.run(["brew", "install", "git"], check=True)

            else:
                self.update_status("Unsupported OS!")
                self.update_progress(0)
                return

            self.update_status("Git installed successfully!")
            self.update_progress(100)

        except subprocess.CalledProcessError as e:
            self.update_status(f"Error: {str(e)}")
            self.update_progress(0)
        finally:
            self.install_button.config(state="normal")

    def update_status(self, message):
        self.status_label.config(text=message)

    def update_progress(self, value):
        self.progress_bar["value"] = value
        self.root.update_idletasks()


# Run the Git Installer UI
if __name__ == "__main__":
    root = tk.Tk()
    app = GitInstallerUI(root)
    root.mainloop()
