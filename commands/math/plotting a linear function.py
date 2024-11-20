# sections: graphing, linear functions

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    try:
        slope = float(entry.get())
        y_intercept = float(entry2.get())

        x = np.linspace(-10, 10, 100)
        y = slope * x + y_intercept

        plt.plot(x, y)
        plt.title(f"Graph of y = {slope}x + {y_intercept}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()

        explanation_text.config(state=tk.NORMAL)
        explanation_text.delete(1.0, tk.END)
        explanation_text.insert(
            tk.END,
            f"Explanation: The graph of a linear function y = mx + b is a straight line.\n\nPython Example:\nimport numpy as np\nimport matplotlib.pyplot as plt\nx = np.linspace(-10, 10, 100)\ny = {slope} * x + {y_intercept}\nplt.plot(x, y)\nplt.show()",
        )
        explanation_text.config(state=tk.DISABLED)
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


def create_ui(root):
    global entry, entry2, result_label, explanation_text

    label = tk.Label(root, text="Enter the slope (m):")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()

    label2 = tk.Label(root, text="Enter the y-intercept (b):")
    label2.pack()
    entry2 = tk.Entry(root)
    entry2.pack()

    plot_button = tk.Button(root, text="Plot Graph", command=plot_graph)
    plot_button.pack()

    result_label = tk.Label(root, text="Graph will appear.")
    result_label.pack()

    explanation_label = tk.Label(root, text="Explanation and Python Example:")
    explanation_label.pack()

    explanation_text = tk.Text(
        root, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED
    )
    explanation_text.pack()


def run_gui():
    root = tk.Tk()
    root.title("Graph of a Linear Function")
    create_ui(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
