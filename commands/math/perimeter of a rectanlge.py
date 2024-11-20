# sections: geometry, perimeter calculation

import tkinter as tk


def calculate_perimeter():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        perimeter = 2 * (length + width)
        result_label.config(text=f"Perimeter: {perimeter} units")
        explanation_text.config(state=tk.NORMAL)
        explanation_text.delete(1.0, tk.END)
        explanation_text.insert(
            tk.END,
            f"Explanation: The perimeter of a rectangle is calculated using the formula P = 2 * (length + width).\n\nPython Example:\nlength = {length}\nwidth = {width}\nperimeter = 2 * (length + width)\n",
        )
        explanation_text.config(state=tk.DISABLED)
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


def create_ui(root):
    global entry_length, entry_width, result_label, explanation_text

    label_length = tk.Label(root, text="Enter the length of the rectangle:")
    label_length.pack()
    entry_length = tk.Entry(root)
    entry_length.pack()

    label_width = tk.Label(root, text="Enter the width of the rectangle:")
    label_width.pack()
    entry_width = tk.Entry(root)
    entry_width.pack()

    solve_button = tk.Button(
        root, text="Calculate Perimeter", command=calculate_perimeter
    )
    solve_button.pack()

    result_label = tk.Label(root, text="Perimeter: ")
    result_label.pack()

    explanation_label = tk.Label(root, text="Explanation and Python Example:")
    explanation_label.pack()

    explanation_text = tk.Text(
        root, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED
    )
    explanation_text.pack()


def run_gui():
    root = tk.Tk()
    root.title("Perimeter of a Rectangle")
    create_ui(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
