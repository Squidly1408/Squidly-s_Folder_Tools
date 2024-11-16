# sections: code, git
import os
import subprocess
import tkinter as tk
from tkinter import messagebox, scrolledtext


def check_status():
    try:
        result = subprocess.run(
            ["git", "status"], check=True, text=True, capture_output=True
        )
        status_output.delete(1.0, tk.END)
        status_output.insert(tk.END, result.stdout)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to retrieve status:\n{e}")


# Create the UI
root = tk.Tk()
root.title("Git Status")
root.geometry("600x400")

tk.Button(root, text="Check Status", command=check_status, font=("Arial", 12)).pack(
    pady=10
)
status_output = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, font=("Arial", 10), width=70, height=20
)
status_output.pack(pady=5)

root.mainloop()
