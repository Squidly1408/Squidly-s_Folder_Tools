# sections: other, code

import tkinter as tk
from tkinter import ttk
import webbrowser


# Create a function to open URLs in a web browser
def open_link(url):
    webbrowser.open(url)


# Define a dictionary with tech stacks and their resources
language_resources = {
    "Python": {
        "resources": [
            ("Official Python Documentation", "https://docs.python.org/3/"),
            ("Learn Python (W3Schools)", "https://www.w3schools.com/python/"),
            (
                "Python for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-python-by-building-projects/",
            ),
            (
                "Python Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/python/",
            ),
        ],
        "image": "python.png",
    },
    "HTML": {
        "resources": [
            (
                "HTML Documentation (MDN)",
                "https://developer.mozilla.org/en-US/docs/Web/HTML",
            ),
            ("Learn HTML (W3Schools)", "https://www.w3schools.com/html/"),
            (
                "HTML Tutorial (freeCodeCamp)",
                "https://www.freecodecamp.org/news/html5-tutorial/",
            ),
            ("HTML Basics (TutorialsPoint)", "https://www.tutorialspoint.com/html/"),
        ],
        "image": "html.png",
    },
    "CSS": {
        "resources": [
            (
                "CSS Documentation (MDN)",
                "https://developer.mozilla.org/en-US/docs/Web/CSS",
            ),
            ("Learn CSS (W3Schools)", "https://www.w3schools.com/css/"),
            (
                "CSS Flexbox (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-css-flexbox-by-building-a-flexbox-portfolio/",
            ),
            ("CSS Tutorials (TutorialsPoint)", "https://www.tutorialspoint.com/css/"),
        ],
        "image": "css.png",
    },
    "JavaScript": {
        "resources": [
            (
                "JavaScript Documentation (MDN)",
                "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
            ),
            ("Learn JavaScript (W3Schools)", "https://www.w3schools.com/js/"),
            (
                "JavaScript for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-javascript-full-course/",
            ),
            (
                "JavaScript Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/javascript/",
            ),
        ],
        "image": "js.png",
    },
    "React": {
        "resources": [
            ("React Documentation", "https://reactjs.org/docs/getting-started.html"),
            (
                "React Tutorial (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-react-by-building-a-simple-app-d8d8b1f56f4f/",
            ),
            ("Learn React (Codecademy)", "https://www.codecademy.com/learn/react-101"),
            (
                "React for Beginners (YouTube)",
                "https://www.youtube.com/results?search_query=react+beginner+tutorial",
            ),
        ],
        "image": "react.png",
    },
    "Ruby": {
        "resources": [
            ("Ruby Documentation", "https://www.ruby-lang.org/en/documentation/"),
            ("Learn Ruby (W3Schools)", "https://www.w3schools.com/ruby/"),
            (
                "Ruby for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/ruby-for-beginners/",
            ),
            ("Ruby Tutorials (TutorialsPoint)", "https://www.tutorialspoint.com/ruby/"),
        ],
        "image": "ruby.png",
    },
    "Rust": {
        "resources": [
            ("Rust Documentation", "https://www.rust-lang.org/learn"),
            ("Learn Rust (W3Schools)", "https://www.w3schools.com/rust/"),
            (
                "Rust Book (The Rust Programming Language)",
                "https://doc.rust-lang.org/book/",
            ),
            ("Rust Tutorials (TutorialsPoint)", "https://www.tutorialspoint.com/rust/"),
        ],
        "image": "rust.png",
    },
    "Java": {
        "resources": [
            ("Java Documentation (Oracle)", "https://docs.oracle.com/en/java/"),
            ("Learn Java (W3Schools)", "https://www.w3schools.com/java/"),
            (
                "Java for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/java-tutorial-for-beginners/",
            ),
            ("Java Tutorials (TutorialsPoint)", "https://www.tutorialspoint.com/java/"),
        ],
        "image": "java.png",
    },
    "C#": {
        "resources": [
            (
                "C# Documentation (Microsoft)",
                "https://learn.microsoft.com/en-us/dotnet/csharp/",
            ),
            ("Learn C# (W3Schools)", "https://www.w3schools.com/cs/"),
            (
                "C# for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/csharp-tutorial-for-beginners/",
            ),
            ("C# Tutorials (TutorialsPoint)", "https://www.tutorialspoint.com/csharp/"),
        ],
        "image": "csharp.png",
    },
    "C++": {
        "resources": [
            ("C++ Documentation (cppreference)", "https://en.cppreference.com/w/"),
            ("Learn C++ (W3Schools)", "https://www.w3schools.com/cpp/"),
            (
                "C++ for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/c-plus-plus-tutorial/",
            ),
            (
                "C++ Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/cplusplus/",
            ),
        ],
        "image": "cpp.png",
    },
    "Kotlin": {
        "resources": [
            ("Kotlin Documentation", "https://kotlinlang.org/docs/home.html"),
            ("Learn Kotlin (W3Schools)", "https://www.w3schools.com/kotlin/"),
            (
                "Kotlin for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-kotlin-by-building-android-apps/",
            ),
            (
                "Kotlin Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/kotlin/",
            ),
        ],
        "image": "kotlin.png",
    },
    "SQL": {
        "resources": [
            ("SQL Documentation (W3Schools)", "https://www.w3schools.com/sql/"),
            ("Learn SQL (TutorialsPoint)", "https://www.tutorialspoint.com/sql/"),
            (
                "SQL for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/sql-for-beginners/",
            ),
            ("SQL Tutorials (SQLZoo)", "https://sqlzoo.net/"),
        ],
        "image": "sql.png",
    },
    "Swift": {
        "resources": [
            ("Swift Documentation", "https://developer.apple.com/swift/"),
            ("Learn Swift (W3Schools)", "https://www.w3schools.com/swift/"),
            (
                "Swift for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-swift-programming/",
            ),
            (
                "Swift Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/swift/",
            ),
        ],
        "image": "swift.png",
    },
    "TypeScript": {
        "resources": [
            ("TypeScript Documentation", "https://www.typescriptlang.org/docs/"),
            ("Learn TypeScript (W3Schools)", "https://www.w3schools.com/typescript/"),
            (
                "TypeScript for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-typescript-by-building-projects/",
            ),
            (
                "TypeScript Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/typescript/",
            ),
        ],
        "image": "typescript.png",
    },
    "PHP": {
        "resources": [
            ("PHP Documentation", "https://www.php.net/docs.php"),
            ("Learn PHP (W3Schools)", "https://www.w3schools.com/php/"),
            (
                "PHP for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-php-with-a-portfolio-project/",
            ),
            ("PHP Tutorials (TutorialsPoint)", "https://www.tutorialspoint.com/php/"),
        ],
        "image": "php.png",
    },
    "JSON": {
        "resources": [
            (
                "JSON Documentation (MDN)",
                "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON",
            ),
            (
                "Learn JSON (W3Schools)",
                "https://www.w3schools.com/js/js_json_intro.asp",
            ),
            (
                "JSON for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-json-in-5-minutes/",
            ),
            ("JSON Tutorials (TutorialsPoint)", "https://www.tutorialspoint.com/json/"),
        ],
        "image": "json.png",
    },
    "R": {
        "resources": [
            ("R Documentation", "https://cran.r-project.org/manuals.html"),
            ("Learn R (W3Schools)", "https://www.w3schools.com/r/"),
            (
                "R for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-r-programming-for-beginners/",
            ),
            ("R Tutorials (TutorialsPoint)", "https://www.tutorialspoint.com/r/"),
        ],
        "image": "r.png",
    },
    "Dart": {
        "resources": [
            ("Dart Documentation", "https://dart.dev/guides"),
            ("Learn Dart (W3Schools)", "https://www.w3schools.com/dart/"),
            (
                "Dart for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/dart-programming-for-beginners/",
            ),
            ("Dart Tutorials (TutorialsPoint)", "https://www.tutorialspoint.com/dart/"),
        ],
        "image": "dart.png",
    },
    "Flutter": {
        "resources": [
            ("Flutter Documentation", "https://flutter.dev/docs"),
            ("Learn Flutter (W3Schools)", "https://www.w3schools.com/flutter/"),
            (
                "Flutter for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-flutter-for-beginners/",
            ),
            (
                "Flutter Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/flutter/",
            ),
        ],
        "image": "flutter.png",
    },
    "Firebase": {
        "resources": [
            ("Firebase Documentation", "https://firebase.google.com/docs"),
            ("Learn Firebase (W3Schools)", "https://www.w3schools.com/firebase/"),
            (
                "Firebase for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-firebase-by-building-an-app/",
            ),
            (
                "Firebase Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/firebase/",
            ),
        ],
        "image": "firebase.png",
    },
    "Git": {
        "resources": [
            ("Git Documentation", "https://git-scm.com/doc"),
            ("Learn Git (W3Schools)", "https://www.w3schools.com/git/"),
            (
                "Git for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/git-and-github-for-beginners/",
            ),
            ("Git Tutorials (TutorialsPoint)", "https://www.tutorialspoint.com/git/"),
        ],
        "image": "git.png",
    },
    "GitHub": {
        "resources": [
            ("GitHub Documentation", "https://docs.github.com/en/github"),
            ("Learn GitHub (W3Schools)", "https://www.w3schools.com/github/"),
            (
                "GitHub for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-github-by-creating-a-repository/",
            ),
            (
                "GitHub Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/github/",
            ),
        ],
        "image": "github.png",
    },
    "Visual Studio Code": {
        "resources": [
            ("VS Code Documentation", "https://code.visualstudio.com/docs"),
            (
                "Learn VS Code (W3Schools)",
                "https://www.w3schools.com/whatis/whatis_vscode.asp",
            ),
            (
                "VS Code for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-vscode-for-beginners/",
            ),
            (
                "VS Code Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/visual_studio_code/",
            ),
        ],
        "image": "vscode.png",
    },
    "PCB Design": {
        "resources": [
            ("PCB Design Tutorial", "https://www.efabless.com/learn/pcb-design/"),
            ("Learn PCB Design (W3Schools)", "https://www.w3schools.com/pcb_design/"),
            (
                "PCB Design for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-pcb-design-with-eagle/",
            ),
            (
                "PCB Design Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/pcb_design/",
            ),
        ],
        "image": "pcb_design.png",
    },
    "Arduino": {
        "resources": [
            ("Arduino Documentation", "https://www.arduino.cc/reference/en/"),
            ("Learn Arduino (W3Schools)", "https://www.w3schools.com/arduino/"),
            (
                "Arduino for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-arduino-for-beginners/",
            ),
            (
                "Arduino Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/arduino/",
            ),
        ],
        "image": "arduino.png",
    },
    "Raspberry Pi": {
        "resources": [
            (
                "Raspberry Pi Documentation",
                "https://www.raspberrypi.org/documentation/",
            ),
            (
                "Learn Raspberry Pi (W3Schools)",
                "https://www.w3schools.com/raspberry_pi/",
            ),
            (
                "Raspberry Pi for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-raspberry-pi-for-beginners/",
            ),
            (
                "Raspberry Pi Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/raspberry_pi/",
            ),
        ],
        "image": "raspberry_pi.png",
    },
    "Linux": {
        "resources": [
            ("Linux Documentation", "https://www.kernel.org/doc/"),
            ("Learn Linux (W3Schools)", "https://www.w3schools.com/linux/"),
            (
                "Linux for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/linux-for-beginners/",
            ),
            (
                "Linux Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/linux/",
            ),
        ],
        "image": "linux.png",
    },
    "AI": {
        "resources": [
            ("AI Documentation", "https://www.ai.gov/"),
            ("Learn AI (W3Schools)", "https://www.w3schools.com/ai/"),
            (
                "AI for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/artificial-intelligence-for-beginners/",
            ),
            (
                "AI Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/artificial_intelligence/",
            ),
        ],
        "image": "ai.png",
    },
    "CAD": {
        "resources": [
            ("CAD Documentation", "https://www.autodesk.com/solutions/cad-software"),
            ("Learn CAD (W3Schools)", "https://www.w3schools.com/cad/"),
            (
                "CAD for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/cad-for-beginners/",
            ),
            ("CAD Tutorials (TutorialsPoint)", "https://www.tutorialspoint.com/cad/"),
        ],
        "image": "cad.png",
    },
    "Angular": {
        "resources": [
            ("Angular Documentation", "https://angular.io/docs"),
            ("Learn Angular (W3Schools)", "https://www.w3schools.com/angular/"),
            (
                "Angular for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-angular-for-beginners/",
            ),
            (
                "Angular Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/angular/",
            ),
        ],
        "image": "angular.png",
    },
    ".NET": {
        "resources": [
            (".NET Documentation", "https://learn.microsoft.com/en-us/dotnet/"),
            (".NET Learn (W3Schools)", "https://www.w3schools.com/dotnet/"),
            (
                ".NET for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-net-for-beginners/",
            ),
            (
                ".NET Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/dotnet/",
            ),
        ],
        "image": "dotnet.png",
    },
    "Electron": {
        "resources": [
            ("Electron Documentation", "https://www.electronjs.org/docs"),
            ("Learn Electron (W3Schools)", "https://www.w3schools.com/electron/"),
            (
                "Electron for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/electron-for-beginners/",
            ),
            (
                "Electron Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/electron/",
            ),
        ],
        "image": "electron.png",
    },
    "MySQL": {
        "resources": [
            ("MySQL Documentation", "https://dev.mysql.com/doc/"),
            ("Learn MySQL (W3Schools)", "https://www.w3schools.com/mysql/"),
            (
                "MySQL for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/mysql-for-beginners/",
            ),
            (
                "MySQL Tutorials (TutorialsPoint)",
                "https://www.tutorialspoint.com/mysql/",
            ),
        ],
        "image": "mysql.png",
    },
    "NPM": {
        "resources": [
            ("NPM Documentation", "https://docs.npmjs.com/"),
            ("Learn NPM (W3Schools)", "https://www.w3schools.com/npm/"),
            (
                "NPM for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/npm-for-beginners/",
            ),
            ("NPM Tutorials (TutorialsPoint)", "https://www.tutorialspoint.com/npm/"),
        ],
        "image": "npm.png",
    },
    "Vue": {
        "resources": [
            ("Vue Documentation", "https://vuejs.org/v2/guide/"),
            ("Learn Vue (W3Schools)", "https://www.w3schools.com/vue/"),
            (
                "Vue for Beginners (freeCodeCamp)",
                "https://www.freecodecamp.org/news/learn-vue-for-beginners/",
            ),
            ("Vue Tutorials (TutorialsPoint)", "https://www.tutorialspoint.com/vuejs/"),
        ],
        "image": "vue.png",
    },
}
# Create the main application window
root = tk.Tk()
root.title("Tech Stack Learning Resources")

# Create a frame for the tech stack list
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="nsew")

# Create a Treeview widget to display tech stack and resources
treeview = ttk.Treeview(frame, columns=("Resource", "Link"), show="headings", height=15)
treeview.grid(row=0, column=0, sticky="nsew")

# Define column headings
treeview.heading("Resource", text="Resource")
treeview.heading("Link", text="Link")

# Configure the columns to make them expand
treeview.column("Resource", width=250, anchor="w")
treeview.column("Link", width=350, anchor="w")


# Function to add resources for a specific tech stack
def add_resources(tech_name):
    # Clear the current treeview
    for row in treeview.get_children():
        treeview.delete(row)

    # Add the resources for the selected tech stack
    for resource, url in language_resources.get(tech_name, {}).get("resources", []):
        treeview.insert("", "end", values=(resource, url))


# Create a dropdown menu to select a tech stack
tech_stack_names = list(language_resources.keys())
tech_stack_var = tk.StringVar(
    value=tech_stack_names[0]
)  # Default to the first tech stack
tech_stack_menu = ttk.Combobox(
    root,
    textvariable=tech_stack_var,
    values=tech_stack_names,
    state="readonly",
    width=40,
)
tech_stack_menu.grid(row=1, column=0, pady=10)


# Add an event listener to update the treeview when a new tech stack is selected
def on_tech_stack_change(event):
    selected_tech = tech_stack_var.get()
    add_resources(selected_tech)


tech_stack_menu.bind("<<ComboboxSelected>>", on_tech_stack_change)

# Initialize with the first tech stack
add_resources(tech_stack_names[0])

# Add a scrollbar for the treeview
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=treeview.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
treeview.configure(yscrollcommand=scrollbar.set)


# Function to handle link clicks
def on_item_click(event):
    item = treeview.selection()[0]  # Get selected item
    link = treeview.item(item, "values")[1]  # Get the URL from the 'Link' column
    if link:
        open_link(link)


# Bind the item click event to open the link
treeview.bind("<Double-1>", on_item_click)

# Start the Tkinter event loop
root.mainloop()
