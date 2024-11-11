import tkinter as tk
from tkinter import messagebox
import subprocess

def clone_repo():
    repo_url = repo_var.get()
    dest_dir = dir_var.get()
    if not repo_url:
        messagebox.showerror("Error", "Please enter the repository URL.")
        return
    try:
        subprocess.run(["git", "clone", repo_url, dest_dir], check=True)
        messagebox.showinfo("Success", f"Repository cloned to {dest_dir}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to clone repository:\n{e}")

root = tk.Tk()
root.title("Clone Git Repository")

tk.Label(root, text="Repository URL:").pack(pady=5)
repo_var = tk.StringVar()
tk.Entry(root, textvariable=repo_var, width=50).pack(pady=5)

tk.Label(root, text="Destination Directory (leave blank for default):").pack(pady=5)
dir_var = tk.StringVar()
tk.Entry(root, textvariable=dir_var, width=50).pack(pady=5)

tk.Button(root, text="Clone", command=clone_repo).pack(pady=20)

root.mainloop()
