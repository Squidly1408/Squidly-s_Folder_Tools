# sections: algebra, quadratic equations

import tkinter as tk
import math


def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        discriminant = b**2 - 4 * a * c
        if discriminant >= 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            result_label.config(text=f"Roots: x1 = {root1}, x2 = {root2}")
        else:
            result_label.config(text="No real roots.")
        explanation_text.config(state=tk.NORMAL)
        explanation_text.delete(1.0, tk.END)
        explanation_text.insert(
            tk.END,
            f"Explanation: The quadratic formula is used to find the roots of a quadratic equation ax² + bx + c = 0.\n\nPython Example:\na = {a}\nb = {b}\nc = {c}\ndiscriminant = b² - 4ac\nroot1 = (-b + √discriminant) / (2a)\nroot2 = (-b - √discriminant) / (2a)\n",
        )
        explanation_text.config(state=tk.DISABLED)
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


def create_ui(root):
    global entry_a, entry_b, entry_c, result_label, explanation_text

    label_a = tk.Label(root, text="Enter coefficient a:")
    label_a.pack()
    entry_a = tk.Entry(root)
    entry_a.pack()

    label_b = tk.Label(root, text="Enter coefficient b:")
    label_b.pack()
    entry_b = tk.Entry(root)
    entry_b.pack()

    label_c = tk.Label(root, text="Enter coefficient c:")
    label_c.pack()
    entry_c = tk.Entry(root)
    entry_c.pack()

    solve_button = tk.Button(
        root, text="Solve Quadratic Equation", command=solve_quadratic
    )
    solve_button.pack()

    result_label = tk.Label(root, text="Roots: ")
    result_label.pack()

    explanation_label = tk.Label(root, text="Explanation and Python Example:")
    explanation_label.pack()

    explanation_text = tk.Text(
        root, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED
    )
    explanation_text.pack()


def run_gui():
    root = tk.Tk()
    root.title("Solve Quadratic Equation")
    create_ui(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
