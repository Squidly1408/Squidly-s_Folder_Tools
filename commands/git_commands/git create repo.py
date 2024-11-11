import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def create_repo():
    repo_dir = dir_var.get()
    if not repo_dir:
        messagebox.showerror("Error", "Please enter the directory to initialize the repository.")
        return
    try:
        os.makedirs(repo_dir, exist_ok=True)
        subprocess.run(["git", "-C", repo_dir, "init"], check=True)
        messagebox.showinfo("Success", f"Git repository initialized in {repo_dir}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to initialize repository:\n{e}")

root = tk.Tk()
root.title("Create Git Repository")

tk.Label(root, text="Directory to Initialize Repository:").pack(pady=5)
dir_var = tk.StringVar()
tk.Entry(root, textvariable=dir_var, width=50).pack(pady=5)

tk.Button(root, text="Create", command=create_repo).pack(pady=20)

root.mainloop()
