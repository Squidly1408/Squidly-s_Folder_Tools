# sections: other

import tkinter as tk
import random


class RandomNumberGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Number Generator")
        self.root.geometry("350x300")
        self.root.configure(bg="#171717")  # Set background color

        # Title Label
        self.title_label = tk.Label(
            self.root,
            text="Generate Random Numbers",
            bg="#171717",
            fg="white",
            font=("Arial", 14, "bold"),
        )
        self.title_label.pack(pady=10)

        # Lower Limit Label and Entry
        self.lower_limit_label = tk.Label(
            self.root,
            text="Lower Limit:",
            bg="#171717",
            fg="white",
            font=("Arial", 12),
        )
        self.lower_limit_label.pack(pady=5)
        self.lower_limit_entry = tk.Entry(
            self.root,
            bg="#171717",
            fg="white",
            font=("Arial", 12),
            borderwidth=0,
            insertbackground="white",
        )
        self.lower_limit_entry.pack(pady=5)

        # Upper Limit Label and Entry
        self.upper_limit_label = tk.Label(
            self.root,
            text="Upper Limit:",
            bg="#171717",
            fg="white",
            font=("Arial", 12),
        )
        self.upper_limit_label.pack(pady=5)
        self.upper_limit_entry = tk.Entry(
            self.root,
            bg="#171717",
            fg="white",
            font=("Arial", 12),
            borderwidth=0,
            insertbackground="white",
        )
        self.upper_limit_entry.pack(pady=5)

        # Label to display the random number
        self.random_number_label = tk.Label(
            self.root,
            text="Enter limits and click 'Generate'",
            bg="#171717",
            fg="white",
            font=("Arial", 12),
        )
        self.random_number_label.pack(pady=10)

        # Generate Button
        self.generate_button = tk.Button(
            self.root,
            text="Generate Random Number",
            command=self.generate_random_number,
            bg="#00796b",
            fg="white",
            font=("Arial", 12),
            relief="flat",
        )
        self.generate_button.pack(pady=10)

    def generate_random_number(self):
        """Generate a random number within the specified range."""
        try:
            lower_limit = int(self.lower_limit_entry.get())
            upper_limit = int(self.upper_limit_entry.get())

            if lower_limit >= upper_limit:
                self.random_number_label.config(
                    text="Error: Lower limit must be less than upper limit."
                )
            else:
                random_number = random.randint(lower_limit, upper_limit)
                self.random_number_label.config(text=f"Random Number: {random_number}")
        except ValueError:
            self.random_number_label.config(
                text="Error: Please enter valid numbers for the limits."
            )


# Function to launch the Random Number Generator UI
def run_random_number_generator():
    root = tk.Tk()
    app = RandomNumberGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    run_random_number_generator()
