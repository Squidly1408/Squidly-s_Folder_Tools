# sections: geometry, volume calculation

import tkinter as tk
import math


def calculate_volume():
    try:
        radius = float(entry_radius.get())
        height = float(entry_height.get())
        volume = math.pi * radius**2 * height
        result_label.config(text=f"Volume: {volume:.2f} cubic units")
        explanation_text.config(state=tk.NORMAL)
        explanation_text.delete(1.0, tk.END)
        explanation_text.insert(
            tk.END,
            f"Explanation: The volume of a cylinder is calculated using the formula V = πr²h, where r is the radius and h is the height.\n\nPython Example:\nradius = {radius}\nheight = {height}\nvolume = math.pi * radius**2 * height\n",
        )
        explanation_text.config(state=tk.DISABLED)
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


def create_ui(root):
    global entry_radius, entry_height, result_label, explanation_text

    label_radius = tk.Label(root, text="Enter the radius of the cylinder:")
    label_radius.pack()
    entry_radius = tk.Entry(root)
    entry_radius.pack()

    label_height = tk.Label(root, text="Enter the height of the cylinder:")
    label_height.pack()
    entry_height = tk.Entry(root)
    entry_height.pack()

    solve_button = tk.Button(root, text="Calculate Volume", command=calculate_volume)
    solve_button.pack()

    result_label = tk.Label(root, text="Volume: ")
    result_label.pack()

    explanation_label = tk.Label(root, text="Explanation and Python Example:")
    explanation_label.pack()

    explanation_text = tk.Text(
        root, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED
    )
    explanation_text.pack()


def run_gui():
    root = tk.Tk()
    root.title("Volume of a Cylinder")
    create_ui(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
