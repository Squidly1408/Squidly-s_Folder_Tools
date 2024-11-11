import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Base templates with widgets for expansion
TEMPLATES_WITH_WIDGETS = {
    "Python": {
        "base": "# Python Template\n\nprint('Hello, World!')\n",
        "widgets": {
            "Function": "def my_function():\n    print('This is a function')\n",
            "Class": "class MyClass:\n    def __init__(self):\n        self.value = 'Hello, World!'\n",
            "File Handling": "with open('example.txt', 'w') as file:\n    file.write('Hello, World!')\n",
        },
    },
    "HTML": {
        "base": "<!DOCTYPE html>\n<html>\n<head>\n    <title>HTML Template</title>\n</head>\n<body>\n    <h1>Hello, World!</h1>\n</body>\n</html>",
        "widgets": {
            "Navbar": "<nav>\n    <ul>\n        <li><a href='#'>Home</a></li>\n        <li><a href='#'>About</a></li>\n        <li><a href='#'>Contact</a></li>\n    </ul>\n</nav>\n",
            "Footer": "<footer>\n    <p>&copy; 2024 Your Website</p>\n</footer>\n",
            "Image Placeholder": "<img src='placeholder.jpg' alt='Placeholder Image'>\n",
        },
    },
    "CSS": {
        "base": "/* CSS Template */\nbody {\n    font-family: Arial, sans-serif;\n    background-color: #f4f4f4;\n}\n",
        "widgets": {
            "Button Styling": "button {\n    background-color: blue;\n    color: white;\n    padding: 10px 20px;\n    border: none;\n    cursor: pointer;\n}\n",
            "Grid Layout": ".container {\n    display: grid;\n    grid-template-columns: 1fr 1fr;\n    gap: 10px;\n}\n",
            "Responsive Design": "@media (max-width: 600px) {\n    body {\n        font-size: 14px;\n    }\n}\n",
        },
    },
    "JavaScript": {
        "base": "// JavaScript Template\nconsole.log('Hello, World!');\n",
        "widgets": {
            "Fetch API": "fetch('https://api.example.com/data')\n    .then(response => response.json())\n    .then(data => console.log(data));\n",
            "Event Listener": "document.getElementById('btn').addEventListener('click', () => {\n    alert('Button clicked!');\n});\n",
            "DOM Manipulation": "document.body.style.backgroundColor = 'lightblue';\n",
        },
    },
    "React": {
        "base": "import React from 'react';\n\nfunction App() {\n    return (\n        <div>\n            <h1>Hello, World!</h1>\n        </div>\n    );\n}\n\nexport default App;\n",
        "widgets": {
            "State Hook": "import { useState } from 'react';\nconst [count, setCount] = useState(0);\n",
            "Effect Hook": "import { useEffect } from 'react';\nuseEffect(() => {\n    console.log('Component mounted');\n}, []);\n",
            "Custom Component": "function MyComponent() {\n    return <div>Custom Component</div>;\n}\nexport default MyComponent;\n",
        },
    },
    "Node.js": {
        "base": "// Node.js Template\nconst express = require('express');\nconst app = express();\n\napp.get('/', (req, res) => {\n    res.send('Hello, World!');\n});\n\napp.listen(3000, () => console.log('Server running on port 3000'));\n",
        "widgets": {
            "Middleware": "app.use((req, res, next) => {\n    console.log('Middleware activated');\n    next();\n});\n",
            "Static Files": "app.use(express.static('public'));\n",
            "REST API Endpoint": "app.get('/api/data', (req, res) => {\n    res.json({ message: 'Hello from API' });\n});\n",
        },
    },
    "C++": {
        "base": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Hello, World!\" << endl;\n    return 0;\n}\n",
        "widgets": {
            "Class": "class MyClass {\n    public:\n        void display() {\n            cout << \"Class Method\" << endl;\n        }\n};\n",
            "File I/O": "#include <fstream>\nofstream outfile(\"example.txt\");\noutfile << \"Hello, World!\";\noutfile.close();\n",
            "STL Vector": "#include <vector>\nvector<int> myVector = {1, 2, 3, 4};\n",
        },
    },
    "Java": {
        "base": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}\n",
        "widgets": {
            "Class": "class MyClass {\n    int value;\n    MyClass(int value) {\n        this.value = value;\n    }\n    void display() {\n        System.out.println(value);\n    }\n}\n",
            "File I/O": "import java.io.*;\nFileWriter writer = new FileWriter(\"example.txt\");\nwriter.write(\"Hello, World!\");\nwriter.close();\n",
            "ArrayList": "import java.util.ArrayList;\nArrayList<String> list = new ArrayList<>();\nlist.add(\"Item 1\");\n",
        },
    },
    "SQL": {
        "base": "-- SQL Template\nCREATE DATABASE example_db;\nUSE example_db;\nCREATE TABLE users (\n    id INT AUTO_INCREMENT PRIMARY KEY,\n    name VARCHAR(100),\n    email VARCHAR(100)\n);\n",
        "widgets": {
            "Insert Statement": "INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');\n",
            "Select Statement": "SELECT * FROM users;\n",
            "Join Query": "SELECT users.name, orders.total FROM users\nJOIN orders ON users.id = orders.user_id;\n",
        },
    },
    "Ruby": {
        "base": "# Ruby Template\nputs 'Hello, World!'\n",
        "widgets": {
            "Method": "def my_method\n    puts 'This is a method'\nend\n",
            "Class": "class MyClass\n    def initialize\n        @value = 'Hello, World!'\n    end\nend\n",
            "File Handling": "File.open('example.txt', 'w') { |file| file.write('Hello, World!') }\n",
        },
    },
    "Go": {
        "base": "// Go Template\npackage main\n\nimport \"fmt\"\n\nfunc main() {\n    fmt.Println(\"Hello, World!\")\n}\n",
        "widgets": {
            "Function": "func myFunction() {\n    fmt.Println(\"This is a function\")\n}\n",
            "Struct": "type MyStruct struct {\n    Name string\n    Age  int\n}\n",
            "File I/O": "file, _ := os.Create(\"example.txt\")\nfile.WriteString(\"Hello, World!\")\nfile.Close()\n",
        },
    },
    "PHP": {
        "base": "<?php\n// PHP Template\necho 'Hello, World!';\n?>",
        "widgets": {
            "Function": "<?php\nfunction myFunction() {\n    echo 'This is a function';\n}\n?>",
            "Database Connection": "<?php\n$conn = new mysqli('localhost', 'user', 'password', 'database');\nif ($conn->connect_error) {\n    die('Connection failed: ' . $conn->connect_error);\n}\n?>",
            "Form Handling": "<?php\nif ($_SERVER['REQUEST_METHOD'] === 'POST') {\n    $name = $_POST['name'];\n    echo 'Hello, ' . $name;\n}\n?>",
        },
    },
    "Kotlin": {
        "base": "fun main() {\n    println(\"Hello, World!\")\n}\n",
        "widgets": {
            "Function": "fun myFunction() {\n    println(\"This is a function\")\n}\n",
            "Class": "class MyClass(val name: String) {\n    fun greet() {\n        println(\"Hello, \$name\")\n    }\n}\n",
            "Coroutines": "import kotlinx.coroutines.*\n\nfun main() = runBlocking {\n    launch {\n        delay(1000L)\n        println(\"Hello from coroutine\")\n    }\n}\n",
        },
    },
    "Swift": {
        "base": "import Foundation\n\nprint(\"Hello, World!\")\n",
        "widgets": {
            "Function": "func myFunction() {\n    print(\"This is a function\")\n}\n",
            "Class": "class MyClass {\n    var value: String\n\n    init(value: String) {\n        self.value = value\n    }\n}\n",
            "Networking": "import Foundation\n\nlet url = URL(string: \"https://example.com\")!\nlet task = URLSession.shared.dataTask(with: url) { data, response, error in\n    if let data = data {\n        print(String(data: data, encoding: .utf8) ?? \"No data\")\n    }\n}\ntask.resume()\n",
        },
    },

    "Rust": {
        "base": "// Rust Template\nfn main() {\n    println!(\"Hello, World!\");\n}\n",
        "widgets": {
            "Function": "fn my_function() {\n    println!(\"This is a function\");\n}\n",
            "Struct": "struct MyStruct {\n    name: String,\n    age: u32,\n}\n",
            "File Handling": "use std::fs::File;\nuse std::io::prelude::*;\n\nfn main() {\n    let mut file = File::create(\"example.txt\").unwrap();\n    file.write_all(b\"Hello, World!\").unwrap();\n}\n",
        },
    },
    "Perl": {
        "base": "# Perl Template\nprint \"Hello, World!\\n\";\n",
        "widgets": {
            "Function": "sub my_function {\n    print \"This is a function\\n\";\n}\n",
            "Array": "@arr = (1, 2, 3, 4);\nforeach $num (@arr) {\n    print \"$num\\n\";\n}\n",
            "File Handling": "open my $fh, '>', 'example.txt' or die \"Can't open file: $!\";\nprint $fh \"Hello, World!\";\nclose $fh;\n",
        },
    },
    "TypeScript": {
        "base": "// TypeScript Template\nconsole.log('Hello, World!');\n",
        "widgets": {
            "Function": "function myFunction() {\n    console.log('This is a function');\n}\n",
            "Class": "class MyClass {\n    constructor(private name: string) {}\n\n    greet() {\n        console.log('Hello, ' + this.name);\n    }\n}\n",
            "Promise": "function fetchData(): Promise<void> {\n    return new Promise((resolve) => {\n        setTimeout(() => {\n            console.log('Data fetched');\n            resolve();\n        }, 1000);\n    });\n}\n",
        },
    },
    "C#": {
        "base": "// C# Template\nusing System;\n\nclass Program {\n    static void Main() {\n        Console.WriteLine(\"Hello, World!\");\n    }\n}\n",
        "widgets": {
            "Function": "using System;\n\nclass Program {\n    static void MyFunction() {\n        Console.WriteLine(\"This is a function\");\n    }\n\n    static void Main() {\n        MyFunction();\n    }\n}\n",
            "Class": "using System;\n\nclass MyClass {\n    public string Name { get; set; }\n\n    public MyClass(string name) {\n        Name = name;\n    }\n}\n",
            "File Handling": "using System.IO;\n\nclass Program {\n    static void Main() {\n        File.WriteAllText(\"example.txt\", \"Hello, World!\");\n    }\n}\n",
        },
    },
    "Shell Script (Bash)": {
        "base": "# Shell Script Template\necho 'Hello, World!'\n",
        "widgets": {
            "Function": "my_function() {\n    echo 'This is a function'\n}\n",
            "Conditionals": "if [ -f \"example.txt\" ]; then\n    echo 'File exists'\nelse\n    echo 'File does not exist'\nfi\n",
            "Loops": "for i in {1..5}; do\n    echo \"Number $i\"\ndone\n",
        },
    },
}

class TemplateCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("Expanded Template Creator")
        self.root.geometry('700x500')
        self.root.configure(bg='#1E1E1E')

        # Title Label
        title_label = tk.Label(
            root, text="Select Technology and Widgets to Generate a Template", bg='#1E1E1E', fg='white', font=('Arial', 14, 'bold')
        )
        title_label.pack(pady=10)

        # Dropdown for technology selection
        self.tech_var = tk.StringVar()
        self.tech_dropdown = ttk.Combobox(
            root, textvariable=self.tech_var, values=list(TEMPLATES_WITH_WIDGETS.keys()), state='readonly', width=50
        )
        self.tech_dropdown.pack(pady=10)
        self.tech_dropdown.set("Select a Technology")
        self.tech_dropdown.bind("<<ComboboxSelected>>", self.load_widgets)

        # Widgets selection area
        self.widgets_frame = tk.Frame(root, bg='#1E1E1E')
        self.widgets_frame.pack(pady=10, fill='both', expand=True)

        self.widgets_vars = {}

        # Folder selection button
        select_folder_button = tk.Button(
            root, text="Select Output Folder", command=self.select_output_folder,
            bg='white', fg='black', borderwidth=2, relief="groove"
        )
        select_folder_button.pack(pady=10)

        # Create template button
        create_button = tk.Button(
            root, text="Create Template", command=self.create_template,
            bg='white', fg='black', borderwidth=2, relief="groove"
        )
        create_button.pack(pady=10)

        # Selected folder label
        self.selected_folder = tk.StringVar()
        self.selected_folder.set("No folder selected.")
        folder_label = tk.Label(
            root, textvariable=self.selected_folder, bg='#1E1E1E', fg='white', wraplength=600
        )
        folder_label.pack(pady=10)

        # Output message
        self.message_label = tk.Label(root, text="", bg='#1E1E1E', fg='white', wraplength=600)
        self.message_label.pack(pady=10)

    def select_output_folder(self):
        """Open a dialog to select the output folder."""
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder.set(folder)
            self.message_label.config(text="Selected folder: " + folder, fg='lightblue')

    def load_widgets(self, event=None):
        """Load available widgets for the selected technology."""
        tech = self.tech_var.get()
        self.widgets_vars.clear()
        for widget in self.widgets_frame.winfo_children():
            widget.destroy()

        if tech in TEMPLATES_WITH_WIDGETS:
            widgets = TEMPLATES_WITH_WIDGETS[tech]["widgets"]
            tk.Label(
                self.widgets_frame, text="Select Widgets:", bg='#1E1E1E', fg='white', font=('Arial', 12)
            ).pack(anchor='w', pady=5)
            for widget_name, _ in widgets.items():
                var = tk.BooleanVar()
                tk.Checkbutton(
                    self.widgets_frame, text=widget_name, variable=var, bg='#1E1E1E', fg='white', selectcolor='#1E1E1E'
                ).pack(anchor='w')
                self.widgets_vars[widget_name] = var

    def create_template(self):
        """Create a template file with selected widgets."""
        tech = self.tech_var.get()
        folder = self.selected_folder.get()

        if tech not in TEMPLATES_WITH_WIDGETS:
            messagebox.showerror("Error", "Please select a valid technology.")
            return

        if folder == "No folder selected.":
            messagebox.showerror("Error", "Please select an output folder.")
            return

        # Build the template
        try:
            template_content = TEMPLATES_WITH_WIDGETS[tech]["base"]
            selected_widgets = [
                widget for widget, var in self.widgets_vars.items() if var.get()
            ]
            for widget in selected_widgets:
                template_content += "\n" + TEMPLATES_WITH_WIDGETS[tech]["widgets"][widget]

            # Save the file
            file_name = f"{tech.lower().replace(' ', '_')}_template"
            extension = {
                "Python": "py", "HTML": "html", "CSS": "css", "JavaScript": "js",
            }.get(tech, "txt")
            file_path = os.path.join(folder, f"{file_name}.{extension}")
            with open(file_path, "w") as file:
                file.write(template_content)

            self.message_label.config(text=f"Template created: {file_path}", fg='green')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create template: {e}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TemplateCreator(root)
    root.mainloop()
