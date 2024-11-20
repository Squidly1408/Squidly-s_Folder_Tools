# sections: arithmetic, basic math

import tkinter as tk


def solve_addition():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
        explanation_text.config(state=tk.NORMAL)
        explanation_text.delete(1.0, tk.END)
        explanation_text.insert(
            tk.END,
            f"Explanation: To solve this, we add {num1} and {num2} together.\n\nPython Example:\nnum1 = {num1}\nnum2 = {num2}\nresult = num1 + num2\n",
        )
        explanation_text.config(state=tk.DISABLED)
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


def create_ui(root):
    global entry1, entry2, result_label, explanation_text

    label1 = tk.Label(root, text="Enter the first number:")
    label1.pack()
    entry1 = tk.Entry(root)
    entry1.pack()

    label2 = tk.Label(root, text="Enter the second number:")
    label2.pack()
    entry2 = tk.Entry(root)
    entry2.pack()

    solve_button = tk.Button(root, text="Solve Addition", command=solve_addition)
    solve_button.pack()

    result_label = tk.Label(root, text="Result: ")
    result_label.pack()

    explanation_label = tk.Label(root, text="Explanation and Python Example:")
    explanation_label.pack()

    explanation_text = tk.Text(
        root, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED
    )
    explanation_text.pack()


def run_gui():
    root = tk.Tk()
    root.title("Addition Solver")
    create_ui(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
