# sections: code, git
import os
import subprocess
import tkinter as tk
from tkinter import messagebox


def push_to_remote():
    remote = remote_name.get()
    branch = branch_name.get()

    if not remote.strip() or not branch.strip():
        messagebox.showerror("Error", "Remote and branch names cannot be empty.")
        return

    try:
        subprocess.run(["git", "push", remote, branch], check=True, text=True)
        messagebox.showinfo("Success", f"Pushed to {remote}/{branch} successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to push changes:\n{e}")


# Create the UI
root = tk.Tk()
root.title("Push to Remote")
root.geometry("400x200")

tk.Label(root, text="Remote Name:", font=("Arial", 12)).pack(pady=5)
remote_name = tk.Entry(root, width=50, font=("Arial", 12))
remote_name.pack(pady=5)

tk.Label(root, text="Branch Name:", font=("Arial", 12)).pack(pady=5)
branch_name = tk.Entry(root, width=50, font=("Arial", 12))
branch_name.pack(pady=5)

tk.Button(root, text="Push", command=push_to_remote, font=("Arial", 12)).pack(pady=10)

root.mainloop()
