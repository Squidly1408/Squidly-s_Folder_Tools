import os
from tkinter import (
    Tk,
    filedialog,
    messagebox,
    PhotoImage,
    Button,
    Frame,
    Label,
    Entry,
    StringVar,
)

IMAGES_PATH = "images"  # Define the images path here


def select_folder():
    root = Tk()
    root.withdraw()  # Hide the root window
    folder_selected = filedialog.askdirectory()
    return folder_selected


def delete_unmatched_files(folder, number):
    file_names = {}

    # Count occurrences of each file name
    for file in os.listdir(folder):
        name, ext = os.path.splitext(file)
        if name in file_names:
            file_names[name].append(file)
        else:
            file_names[name] = [file]

    # Delete files that do not meet the required number of occurrences
    for name, files in file_names.items():
        if len(files) < number:
            for file in files:
                os.remove(os.path.join(folder, file))


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Squidly's Folder Tools")
        self.root.geometry("400x300")
        self.root.configure(bg="#171717")
        self.root.overrideredirect(True)

        self.folder = None
        self.num_files = None

        self.create_custom_title_bar()
        self.create_ui()

    def create_custom_title_bar(self):
        """Create a custom title bar with a close button."""
        title_bar = Frame(self.root, bg="#00796b", relief="flat", height=30)
        title_bar.pack(fill="x", side="top")

        title_label = Label(
            title_bar,
            text="Squidly's Folder Tools",
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        title_label.pack(side="left", padx=10)

        close_button = Button(
            title_bar,
            text="X",
            command=self.root.destroy,
            bg="#00796b",
            fg="white",
            font=("Arial", 10, "bold"),
            borderwidth=0,
            highlightthickness=0,
        )
        close_button.pack(side="right", padx=10)

        # Allow dragging the window
        title_bar.bind("<B1-Motion>", self.move_window)
        title_bar.bind("<ButtonPress-1>", self.get_mouse_position)

    def get_mouse_position(self, event):
        self.x = event.x
        self.y = event.y

    def move_window(self, event):
        x = event.x_root - self.x
        y = event.y_root - self.y
        self.root.geometry(f"+{x}+{y}")

    def create_ui(self):
        def select_folder_button():
            self.folder = select_folder()
            if not self.folder:
                messagebox.showerror("Error", "Please select a folder.")

        def start_processing():
            try:
                self.num_files = int(num_files_var.get())
                if not self.folder:
                    messagebox.showerror("Error", "Please select a folder first.")
                else:
                    delete_unmatched_files(self.folder, self.num_files)
                    messagebox.showinfo("Success", "Files processed successfully.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")

        # Add UI components
        frame = Frame(self.root, bg="#171717")
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        folder_image = PhotoImage(file=f"{IMAGES_PATH}/folder.png")
        folder_button = Button(
            frame,
            text="Select folder",
            image=folder_image,
            compound="top",
            command=select_folder_button,
            bg="#171717",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
        )
        folder_button.image = (
            folder_image  # Keep a reference to prevent garbage collection
        )
        folder_button.pack(pady=20)

        label = Label(
            frame,
            text="How many names have to be the same?",
            bg="#171717",
            fg="white",
            font=("Arial", 12),
        )
        label.pack(pady=10)

        num_files_var = StringVar()
        num_files_entry = Entry(
            frame,
            textvariable=num_files_var,
            bg="#171717",
            fg="white",
            font=("Arial", 12),
            insertbackground="white",
        )
        num_files_entry.pack(pady=5)

        # Add placeholder text in the entry
        num_files_entry.insert(0, "number...")

        start_button = Button(
            frame,
            text="Start",
            command=start_processing,
            bg="#00796b",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
        )
        start_button.pack(pady=10)


def main():
    root = Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
