# sections: geometry, area calculation

import tkinter as tk
import math


def calculate_area():
    try:
        radius = float(entry.get())
        area = math.pi * radius**2
        result_label.config(text=f"Area: {area:.2f} square units")
        explanation_text.config(state=tk.NORMAL)
        explanation_text.delete(1.0, tk.END)
        explanation_text.insert(
            tk.END,
            f"Explanation: The area of a circle is calculated using the formula A = πr², where r is the radius.\n\nPython Example:\nimport math\nradius = {radius}\narea = math.pi * radius ** 2\n",
        )
        explanation_text.config(state=tk.DISABLED)
    except ValueError:
        result_label.config(text="Please enter a valid radius!")


def create_ui(root):
    global entry, result_label, explanation_text

    label = tk.Label(root, text="Enter the radius of the circle:")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()

    solve_button = tk.Button(root, text="Calculate Area", command=calculate_area)
    solve_button.pack()

    result_label = tk.Label(root, text="Area: ")
    result_label.pack()

    explanation_label = tk.Label(root, text="Explanation and Python Example:")
    explanation_label.pack()

    explanation_text = tk.Text(
        root, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED
    )
    explanation_text.pack()


def run_gui():
    root = tk.Tk()
    root.title("Area of a Circle")
    create_ui(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
