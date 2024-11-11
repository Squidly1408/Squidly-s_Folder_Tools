import tkinter as tk
from tkinter import messagebox
import subprocess

def pull_repo():
    repo_dir = dir_var.get()
    if not repo_dir:
        messagebox.showerror("Error", "Please enter the repository directory.")
        return
    try:
        subprocess.run(["git", "-C", repo_dir, "pull"], check=True)
        messagebox.showinfo("Success", "Repository updated successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to pull repository:\n{e}")

root = tk.Tk()
root.title("Pull Git Repository")

tk.Label(root, text="Repository Directory:").pack(pady=5)
dir_var = tk.StringVar()
tk.Entry(root, textvariable=dir_var, width=50).pack(pady=5)

tk.Button(root, text="Pull", command=pull_repo).pack(pady=20)

root.mainloop()
