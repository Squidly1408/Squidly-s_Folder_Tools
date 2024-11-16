# sections: code, git
import os
import subprocess
import tkinter as tk
from tkinter import messagebox


def commit_changes():
    message = commit_message.get()
    if not message.strip():
        messagebox.showerror("Error", "Commit message cannot be empty.")
        return

    try:
        subprocess.run(["git", "add", "."], check=True, text=True)
        subprocess.run(["git", "commit", "-m", message], check=True, text=True)
        messagebox.showinfo("Success", "Changes committed successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to commit changes:\n{e}")


# Create the UI
root = tk.Tk()
root.title("Commit Changes")
root.geometry("400x200")

tk.Label(root, text="Commit Message:", font=("Arial", 12)).pack(pady=5)
commit_message = tk.Entry(root, width=50, font=("Arial", 12))
commit_message.pack(pady=5)

tk.Button(root, text="Commit", command=commit_changes, font=("Arial", 12)).pack(pady=10)

root.mainloop()
