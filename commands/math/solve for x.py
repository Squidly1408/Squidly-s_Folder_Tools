# sections: algebra, basic equations

import tkinter as tk
from sympy import symbols, Eq, solve


def solve_equation():
    try:
        # Read input
        coefficient = float(entry.get())
        constant = float(entry2.get())

        x = symbols("x")
        equation = Eq(coefficient * x, constant)
        solution = solve(equation, x)[0]

        result_label.config(text=f"Solution: x = {solution}")
        explanation_text.config(state=tk.NORMAL)
        explanation_text.delete(1.0, tk.END)
        explanation_text.insert(
            tk.END,
            f"Explanation: To solve {coefficient}x = {constant}, we isolate x.\n\nPython Example:\nfrom sympy import symbols, Eq, solve\nx = symbols('x')\nequation = Eq({coefficient} * x, {constant})\nsolution = solve(equation, x)\n",
        )
        explanation_text.config(state=tk.DISABLED)
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


def create_ui(root):
    global entry, entry2, result_label, explanation_text

    label = tk.Label(root, text="Enter coefficient of x:")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()

    label2 = tk.Label(root, text="Enter constant:")
    label2.pack()
    entry2 = tk.Entry(root)
    entry2.pack()

    solve_button = tk.Button(root, text="Solve Equation", command=solve_equation)
    solve_button.pack()

    result_label = tk.Label(root, text="Solution: ")
    result_label.pack()

    explanation_label = tk.Label(root, text="Explanation and Python Example:")
    explanation_label.pack()

    explanation_text = tk.Text(
        root, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED
    )
    explanation_text.pack()


def run_gui():
    root = tk.Tk()
    root.title("Solve for x")
    create_ui(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
