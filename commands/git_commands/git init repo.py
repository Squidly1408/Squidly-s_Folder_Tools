# sections: code, git
import os
import subprocess
import tkinter as tk
from tkinter import messagebox


def init_repo():
    repo_path = entry.get()
    if not repo_path.strip():
        messagebox.showerror("Error", "Repository path cannot be empty.")
        return

    try:
        subprocess.run(["git", "init", repo_path], check=True, text=True)
        messagebox.showinfo("Success", f"Initialized a Git repository at {repo_path}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to initialize repository:\n{e}")


# Create the UI
root = tk.Tk()
root.title("Initialize Git Repository")
root.geometry("400x150")

tk.Label(root, text="Repository Path:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Initialize", command=init_repo, font=("Arial", 12)).pack(pady=10)

root.mainloop()
