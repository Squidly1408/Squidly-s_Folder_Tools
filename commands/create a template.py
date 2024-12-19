# sections: folders, code

import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Base templates with widgets for expansion
TEMPLATES_WITH_WIDGETS = {
    "Electron": {
        "base": "// Electron Template\nconst { app, BrowserWindow } = require('electron');\n\nfunction createWindow() {\n  let win = new BrowserWindow({\n    width: 800,\n    height: 600,\n    webPreferences: {\n      nodeIntegration: true\n    }\n  });\n\n  win.loadURL('http://localhost:3000');\n}\n\napp.whenReady().then(() => {\n  createWindow();\n  app.on('activate', () => {\n    if (BrowserWindow.getAllWindows().length === 0) createWindow();\n  });\n});\n\napp.on('window-all-closed', () => {\n  if (process.platform !== 'darwin') app.quit();\n});",
        "widgets": {
            "Window Creation": "const { BrowserWindow } = require('electron');\n\nfunction createWindow() {\n  let win = new BrowserWindow({\n    width: 800,\n    height: 600,\n    webPreferences: {\n      nodeIntegration: true\n    }\n  });\n  win.loadURL('https://your-webpage.com');\n}",
            "Menu": "const { Menu } = require('electron');\n\nconst menu = Menu.buildFromTemplate([{\n  label: 'File',\n  submenu: [\n    { label: 'Quit', role: 'quit' }\n  ]\n}]);\nMenu.setApplicationMenu(menu);",
            "IPC Main (Renderer Communication)": "const { ipcMain } = require('electron');\nipcMain.on('toMain', (event, arg) => {\n  console.log(arg); // Prints message from renderer\n});",
            "Dialog Box": "const { dialog } = require('electron');\n\ndialog.showMessageBox({\n  type: 'info',\n  title: 'Information',\n  message: 'This is an info message.'\n});",
            "Tray Icon": "const { Tray, Menu } = require('electron');\n\nlet tray = new Tray('path/to/icon.png');\nconst contextMenu = Menu.buildFromTemplate([{\n  label: 'Exit', click: () => { app.quit(); }\n}]);\ntray.setToolTip('Electron App');\ntray.setContextMenu(contextMenu);",
            "Auto Update": "const { autoUpdater } = require('electron');\n\nautoUpdater.checkForUpdatesAndNotify();\n\nautoUpdater.on('update-available', () => {\n  console.log('Update available');\n});\nautoUpdater.on('update-downloaded', () => {\n  autoUpdater.quitAndInstall();\n});",
        },
    },
    "MySQL": {
        "base": "# MySQL Template\n# Setting up queries and database connections.\n",
        "widgets": {
            "Create Table": "CREATE TABLE users (\n  id INT AUTO_INCREMENT PRIMARY KEY,\n  name VARCHAR(100),\n  email VARCHAR(100) NOT NULL\n);",
            "Insert Data": "INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');",
            "Select Data": "SELECT * FROM users WHERE email = 'john@example.com';",
            "Update Data": "UPDATE users SET name = 'Jane Doe' WHERE id = 1;",
            "Delete Data": "DELETE FROM users WHERE id = 1;",
            "Join Tables": "SELECT users.name, orders.amount FROM users JOIN orders ON users.id = orders.user_id;",
        },
    },
    "NPM": {
        "base": "// NPM Template\n// Configure package.json and manage Node.js dependencies.\n",
        "widgets": {
            "Install Package": "npm install express",
            "Create Package": "npm init -y",
            "Install Dev Dependency": "npm install --save-dev jest",
            "Run Script": "npm run start",
            "Update Package": "npm update",
            "Uninstall Package": "npm uninstall lodash",
        },
    },
    "React": {
        "base": "// React Template\nimport React from 'react';\nfunction App() {\n  return <h1>Hello, World!</h1>;\n}\nexport default App;",
        "widgets": {
            "Component": "const MyComponent = () => {\n  return <div>My Component</div>;\n};",
            "State": "const [count, setCount] = useState(0);",
            "Event Handling": "const handleClick = () => {\n  console.log('Button clicked');\n};",
            "Effect Hook": "useEffect(() => {\n  console.log('Component mounted');\n}, []);",
            "Form Handling": "const [input, setInput] = useState('');\nconst handleChange = (e) => setInput(e.target.value);",
            "Context API": "const UserContext = createContext();",
        },
    },
    "Vue": {
        "base": "// Vue Template\n<template>\n  <div>Hello, World!</div>\n</template>\n<script>\nexport default {\n  data() {\n    return {\n      message: 'Hello World'\n    };\n  }\n};\n</script>",
        "widgets": {
            "Component": "<template>\n  <div>{{ message }}</div>\n</template>\n<script>\nexport default {\n  data() {\n    return {\n      message: 'Hello from Vue!'\n    };\n  }\n};\n</script>",
            "Event Binding": "<button @click='handleClick'>Click Me</button>\nmethods: {\n  handleClick() {\n    alert('Button clicked');\n  }\n}",
            "Computed Property": "computed: {\n  reversedMessage() {\n    return this.message.split('').reverse().join('');\n  }\n}",
            "Watchers": "watch: {\n  message(newVal) {\n    console.log('Message changed to', newVal);\n  }\n}",
            "Vuex State": "const store = new Vuex.Store({\n  state: {\n    count: 0\n  },\n  mutations: {\n    increment(state) {\n      state.count++;\n    }\n  }\n});",
            "Router": "const routes = [{ path: '/', component: Home }];\nconst router = new VueRouter({ routes });",
        },
    },
    "Swift": {
        "base": "// Swift Template\nimport UIKit\nclass ViewController: UIViewController {\n  override func viewDidLoad() {\n    super.viewDidLoad()\n    print('Hello, World!')\n  }\n}",
        "widgets": {
            "Button Action": "let button = UIButton()\nbutton.addTarget(self, action: #selector(buttonPressed), for: .touchUpInside)",
            "Table View": "let tableView = UITableView()\ntableView.dataSource = self\n",
            "Label Setup": "let label = UILabel()\nlabel.text = 'Hello, World!'",
            "Gesture Recognizer": "let tapGesture = UITapGestureRecognizer(target: self, action: #selector(handleTap))",
            "Auto Layout": "view.addSubview(label)\nlabel.translatesAutoresizingMaskIntoConstraints = false\nNSLayoutConstraint.activate([\n  label.centerXAnchor.constraint(equalTo: view.centerXAnchor),\n  label.centerYAnchor.constraint(equalTo: view.centerYAnchor)\n])",
            "Core Data": "let context = persistentContainer.viewContext",
        },
    },
    "TypeScript": {
        "base": "// TypeScript Template\nlet greeting: string = 'Hello, World!';\nconsole.log(greeting);",
        "widgets": {
            "Class": "class Person {\n  name: string;\n  constructor(name: string) {\n    this.name = name;\n  }\n}",
            "Function": "function greet(name: string): string {\n  return `Hello, ${name}!`;\n}",
            "Interface": "interface Person {\n  name: string;\n  age: number;\n}",
            "Generics": "function identity<T>(arg: T): T {\n  return arg;\n}",
            "Array": "let numbers: number[] = [1, 2, 3];",
            "Promise": "let promise: Promise<string> = new Promise((resolve, reject) => {\n  resolve('Resolved!');\n});",
        },
    },
    "JSON": {
        "base": '// JSON Template\n{\n  "name": "John Doe",\n  "age": 30,\n  "city": "New York"\n}',
        "widgets": {
            "Array": '[\n  {"name": "John"},\n  {"name": "Jane"}\n]',
            "Nested Object": '{\n  "person": {\n    "name": "John",\n    "address": {\n      "street": "123 Main St",\n      "city": "New York"\n    }\n  }\n}',
            "Boolean": '{\n  "isActive": true\n}',
            "Integer": '{\n  "age": 30\n}',
            "String": '{\n  "name": "John Doe"\n}',
            "Null": '{\n  "middleName": null\n}',
        },
    },
    "Visual Studio Code": {
        "base": "// Visual Studio Code Template\n// This is where you can add your settings, snippets, and extensions.",
        "widgets": {
            "Task Runner": '{\n  "version": "2.0.0",\n  "tasks": [\n    {\n      "label": "Build Project",\n      "type": "shell",\n      "command": "npm run build"\n    }\n  ]\n}',
            "Launch Config": '{\n  "version": "0.2.0",\n  "configurations": [\n    {\n      "name": "Launch Program",\n      "type": "node",\n      "request": "launch",\n      "program": "\${workspaceFolder}/index.js"\n    }\n  ]\n}',
            "Settings": '{\n  "editor.fontSize": 14,\n  "editor.wordWrap": "on"\n}',
            "Snippets": '{\n  "javascript": {\n    "Print to Console": {\n      "prefix": "log",\n      "body": "console.log(\\"$1\\");"\n    }\n  }\n}',
            "Extensions": '[\n  "ms-vscode.vscode-typescript-next",\n  "esbenp.prettier-vscode"\n]',
            "User Settings": '{\n  "files.autoSave": "onWindowChange",\n  "editor.formatOnSave": true\n}',
        },
    },
    "PCB Design": {
        "base": "// PCB Design Template\n// This is where you can define components, traces, and layout in your design software.",
        "widgets": {
            "Component": "component('Resistor') {\n    value = '10k';\n    footprint = '0805';\n}",
            "Netlist": "netlist {\n    net1 = { 'R1', 'C1' };\n    net2 = { 'U1', 'R2' };\n}",
            "Schematic": "schematic {\n    R1 = Resistor('10k');\n    C1 = Capacitor('100nF');\n}",
            "Layer Setup": "layer('Top') {\n    traces = 0.15mm;\n    copperFill = true;\n}",
            "Via Setup": "via('THT') {\n    hole = 1mm;\n    pad = 3mm;\n}",
            "Ground Plane": "plane('GND') {\n    fill = 'Copper';\n    clearance = 0.2mm;\n}",
        },
    },
    "Arduino": {
        "base": "// Arduino Template\nvoid setup() {\n  Serial.begin(9600);\n  pinMode(13, OUTPUT);\n}\nvoid loop() {\n  digitalWrite(13, HIGH);\n  delay(1000);\n  digitalWrite(13, LOW);\n  delay(1000);\n}",
        "widgets": {
            "LED Blink": "digitalWrite(13, HIGH);\ndelay(1000);\ndigitalWrite(13, LOW);\ndelay(1000);",
            "Button Press": "if (digitalRead(buttonPin) == HIGH) {\n  Serial.println('Button Pressed');\n}",
            "Servo Control": "Servo myServo;\nmyServo.attach(9);\nmyServo.write(90);",
            "Analog Read": "int sensorValue = analogRead(A0);\nSerial.println(sensorValue);",
            "Serial Monitor": "Serial.begin(9600);\nSerial.println('Hello World');",
            "Interrupts": "attachInterrupt(digitalPinToInterrupt(2), ISR, RISING);",
        },
    },
    "Raspberry Pi": {
        "base": "# Raspberry Pi Template\n# Running scripts on Raspberry Pi\n",
        "widgets": {
            "GPIO Setup": "import RPi.GPIO as GPIO\nGPIO.setmode(GPIO.BCM)\nGPIO.setup(17, GPIO.OUT)",
            "Reading Pin": "input_state = GPIO.input(17)\nif input_state == GPIO.HIGH:\n    print('Button Pressed')",
            "PWM": "pwm = GPIO.PWM(18, 50)\npwm.start(0)\npwm.ChangeDutyCycle(50)",
            "SPI Setup": "import spidev\nspi = spidev.SpiDev()\nspi.open(0,0)\nspi.max_speed_hz = 50000",
            "I2C Setup": "import smbus\nbus = smbus.SMBus(1)\naddress = 0x48\nbus.write_byte(address, 0x01)",
            "Camera": "import picamera\ncamera = picamera.PICamera()\ncamera.capture('image.jpg')",
        },
    },
    "Linux": {
        "base": "# Linux Template\n# Running commands on Linux terminal\n",
        "widgets": {
            "File Navigation": "cd /path/to/directory\nls -l",
            "File Permissions": "chmod 755 myscript.sh",
            "Package Install": "sudo apt-get install package-name",
            "System Info": "top\nuname -a\nfree -h",
            "Service Start": "sudo service apache2 start",
            "Create File": "touch newfile.txt\nnano newfile.txt",
        },
    },
    "AI": {
        "base": "# AI Template\n# This is where you can train and run machine learning models.\n",
        "widgets": {
            "Model Training": "from sklearn.ensemble import RandomForestClassifier\nmodel = RandomForestClassifier()\nmodel.fit(X_train, y_train)",
            "Prediction": "predictions = model.predict(X_test)\nprint(predictions)",
            "Data Preprocessing": "from sklearn.preprocessing import StandardScaler\nscaler = StandardScaler()\nscaled_data = scaler.fit_transform(data)",
            "Neural Network": "import tensorflow as tf\nmodel = tf.keras.models.Sequential([tf.keras.layers.Dense(64, activation='relu'), tf.keras.layers.Dense(10, activation='softmax')])",
            "Cross Validation": "from sklearn.model_selection import cross_val_score\nscore = cross_val_score(model, X, y, cv=5)",
            "Hyperparameter Tuning": "from sklearn.model_selection import GridSearchCV\nparam_grid = {'n_estimators': [100, 200]}\ngrid = GridSearchCV(model, param_grid, cv=3)\ngrid.fit(X_train, y_train)",
        },
    },
    "CAD": {
        "base": "// CAD Template\n// 3D Model or schematic design scripts\n",
        "widgets": {
            "Create Object": "object = new Object3D();\nobject.setShape('Cube');",
            "Set Dimensions": "object.setDimensions(10, 20, 30);",
            "Rotate Object": "object.rotate(45, 0, 0);",
            "Add Texture": "object.setTexture('wood.jpg');",
            "Export Model": "exportModel(object, 'STL');",
            "Add Light": "scene.add(new Light());",
        },
    },
    "Angular": {
        "base": "// Angular Template\nimport { Component } from '@angular/core';\n@Component({\n  selector: 'app-root',\n  templateUrl: './app.component.html',\n  styleUrls: ['./app.component.css']\n})\nexport class AppComponent {\n  title = 'Hello World';\n}",
        "widgets": {
            "Component": "@Component({\n  selector: 'app-name',\n  template: '<h1>{{title}}</h1>',\n  styleUrls: ['./name.component.css']\n})\nexport class NameComponent { title = 'Component'; }",
            "Service": "@Injectable({ providedIn: 'root' })\nexport class DataService { getData() { return of('Data'); }}",
            "Directive": "@Directive({ selector: '[appHighlight]' })\nexport class HighlightDirective { constructor(private el: ElementRef) {\n    el.nativeElement.style.backgroundColor = 'yellow';\n  }}",
            "Pipe": "@Pipe({name: 'reverse'})\nexport class ReversePipe implements PipeTransform {\n  transform(value: string): string {\n    return value.split('').reverse().join('');\n  }}",
            "Routing": "const routes: Routes = [\n  { path: 'home', component: HomeComponent },\n  { path: '', redirectTo: '/home', pathMatch: 'full' }\n];",
            "Forms": '@Component({\n  selector: \'app-form\',\n  template: \'<form (ngSubmit)="onSubmit()"><input [(ngModel)]="name" name="name"></form>\'\n})',
        },
    },
    ".NET": {
        "base": '// .NET Template\nusing System;\nclass Program {\n    static void Main() {\n        Console.WriteLine("Hello, World!");\n    }\n}',
        "widgets": {
            "Class": "class MyClass {\n    public int MyProperty { get; set; }\n}",
            "Method": 'public void MyMethod() {\n    Console.WriteLine("Method called");\n}',
            "Condition": 'if (x > 10) {\n    Console.WriteLine("Greater");\n}',
            "Loop": "for (int i = 0; i < 10; i++) {\n    Console.WriteLine(i);\n}",
            "List": "List<int> myList = new List<int>{ 1, 2, 3 };\nmyList.Add(4);",
            "Async Task": 'public async Task MyTask() {\n    await Task.Delay(1000);\n    Console.WriteLine("Task completed");\n}',
        },
    },
    "CSS": {
        "base": "/* CSS Template */\nbody {\n    font-family: Arial, sans-serif;\n    background-color: #f0f0f0;\n}",
        "widgets": {
            "Background Color": "body {\n    background-color: #ff5733;\n}",
            "Text Color": "p {\n    color: #333;\n}",
            "Font Size": "h1 {\n    font-size: 36px;\n}",
            "Margin and Padding": "div {\n    margin: 10px;\n    padding: 20px;\n}",
            "Flexbox": ".container {\n    display: flex;\n    justify-content: space-between;\n}",
            "Hover Effect": "button:hover {\n    background-color: #008cba;\n}",
        },
    },
    "PHP": {
        "base": "<?php\n// PHP Template\necho 'Hello, World!';\n?>",
        "widgets": {
            "Function": "function myFunction() {\n    echo 'This is a function';\n}",
            "Array": "$arr = array(1, 2, 3, 4);",
            "Condition": "if ($x > 10) {\n    echo 'Greater';\n} else {\n    echo 'Smaller';\n}",
            "Loop": "for ($i = 0; $i < 5; $i++) {\n    echo $i;\n}",
            "Class": "class Person {\n    public $name;\n    public $age;\n}",
            "File Handling": "$file = fopen('test.txt', 'w');\nfwrite($file, 'Hello, World!');\n",
        },
    },
    "JSON": {
        "base": '{\n    "greeting": "Hello, World!"\n}',
        "widgets": {
            "Object": '{\n    "name": "John",\n    "age": 30\n}',
            "Array": "[1, 2, 3, 4]",
            "Nested Object": '{\n    "person": {\n        "name": "John",\n        "age": 30\n    }\n}',
            "Boolean": '{\n    "isActive": true\n}',
            "Null": '{\n    "data": null\n}',
            "Array of Objects": '[\n    {"name": "John", "age": 30},\n    {"name": "Jane", "age": 25}\n]',
        },
    },
    "R": {
        "base": "# R Template\nprint('Hello, World!')\n",
        "widgets": {
            "Function": "my_function <- function() {\n    print('This is a function')\n}",
            "Vector": "my_vector <- c(1, 2, 3, 4)",
            "Matrix": "my_matrix <- matrix(1:9, nrow=3, ncol=3)",
            "Loop": "for (i in 1:5) {\n    print(i)\n}",
            "Condition": "if (x > 10) {\n    print('Greater')\n} else {\n    print('Smaller')\n}",
            "File Handling": "write.csv(my_data, 'output.csv')",
        },
    },
    "Dart": {
        "base": "// Dart Template\nvoid main() {\n  print('Hello, World!');\n}",
        "widgets": {
            "Function": "void myFunction() {\n  print('This is a function');\n}",
            "List": "List<int> myList = [1, 2, 3, 4];",
            "Loop": "for (int i = 0; i < 5; i++) {\n  print(i);\n}",
            "Condition": "if (x > 10) {\n  print('Greater');\n} else {\n  print('Smaller');\n}",
            "Class": "class Person {\n  String name;\n  int age;\n  Person(this.name, this.age);\n}",
            "File Handling": "import 'dart:io';\nFile('test.txt').writeAsString('Hello, World!');",
        },
    },
    "Flutter": {
        "base": "// Flutter Template\nimport 'package:flutter/material.dart';\nvoid main() {\n  runApp(MyApp());\n}\nclass MyApp extends StatelessWidget {\n  @override\n  Widget build(BuildContext context) {\n    return MaterialApp(\n      home: Scaffold(\n        appBar: AppBar(title: Text('Hello, World!')),\n        body: Center(child: Text('Welcome to Flutter!')),\n      ),\n    );\n  }\n}",
        "widgets": {
            "Text Widget": "Text('Hello, World!')",
            "Button": "ElevatedButton(onPressed: () {}, child: Text('Click Me'))",
            "Container": "Container(\n  width: 200,\n  height: 100,\n  color: Colors.blue,\n)",
            "Column": "Column(\n  children: [Text('Item 1'), Text('Item 2')],\n)",
            "Row": "Row(\n  children: [Icon(Icons.home), Icon(Icons.star)],\n)",
            "Image": "Image.asset('assets/image.png')",
        },
    },
    "Firebase": {
        "base": "// Firebase Template\nimport 'package:firebase_core/firebase_core.dart';\nvoid main() async {\n  await Firebase.initializeApp();\n  runApp(MyApp());\n}",
        "widgets": {
            "Initialize Firebase": "await Firebase.initializeApp();",
            "Firestore Get Data": "FirebaseFirestore.instance.collection('users').get();",
            "Firestore Add Data": "FirebaseFirestore.instance.collection('users').add({'name': 'John', 'age': 30});",
            "Authentication": "await FirebaseAuth.instance.signInWithEmailAndPassword(email: 'user@example.com', password: 'password');",
            "Realtime Database": "FirebaseDatabase.instance.reference().child('users').set({'name': 'John'});",
            "Cloud Storage": "FirebaseStorage.instance.ref().child('profile_pics/user1.jpg').putFile(file);",
        },
    },
    "Firebase Auth": {
        "base": "// Firebase Auth Template\nimport 'package:firebase_auth/firebase_auth.dart';\nvoid main() async {\n  FirebaseAuth auth = FirebaseAuth.instance;\n  await auth.signInWithEmailAndPassword(email: 'user@example.com', password: 'password');\n}",
        "widgets": {
            "Sign Up": "UserCredential user = await FirebaseAuth.instance.createUserWithEmailAndPassword(email: 'email', password: 'password');",
            "Sign In": "UserCredential user = await FirebaseAuth.instance.signInWithEmailAndPassword(email: 'email', password: 'password');",
            "Sign Out": "await FirebaseAuth.instance.signOut();",
            "Current User": "User? user = FirebaseAuth.instance.currentUser;",
            "Password Reset": "await FirebaseAuth.instance.sendPasswordResetEmail(email: 'email');",
            "User State": "FirebaseAuth.instance.authStateChanges().listen((User? user) {\n  if (user == null) {\n    print('User is signed out');\n  } else {\n    print('User is signed in');\n  }\n});",
        },
    },
    "Git": {
        "base": "# Git Template\n// Git Initialization and basic commands\n",
        "widgets": {
            "Initialize Repo": "git init",
            "Add Changes": "git add .",
            "Commit Changes": "git commit -m 'Initial commit'",
            "Push to Remote": "git push origin main",
            "Clone Repo": "git clone https://github.com/username/repository.git",
            "Check Status": "git status",
        },
    },
    "GitHub": {
        "base": "# GitHub Template\n// GitHub repository management\n",
        "widgets": {
            "Create New Repo": "Create a new repository on GitHub and initialize it with a README.",
            "Fork Repo": "Go to the repository and click on the 'Fork' button to create your own copy.",
            "Pull Request": "Submit a pull request to merge changes from your branch to the main branch.",
            "Collaborators": "Add collaborators to your repository under Settings > Collaborators.",
            "GitHub Actions": "Set up workflows for continuous integration and deployment using GitHub Actions.",
            "Release": "Create a release on GitHub to package your project's versions.",
        },
    },
    "Ruby": {
        "base": "# Ruby Template\nputs 'Hello, World!'\n",
        "widgets": {
            "Function": "def my_function\n  puts 'This is a function'\nend",
            "Array": "arr = [1, 2, 3, 4]",
            "Hash": "hash = { name: 'John', age: 30 }",
            "Loop": "for i in 1..5\n  puts i\nend",
            "Condition": "if x > 10\n  puts 'Greater'\nelse\n  puts 'Smaller'\nend",
            "File Handling": "File.open('test.txt', 'w') { |f| f.write('Hello, World!') }",
        },
    },
    "Rust": {
        "base": '# Rust Template\nfn main() {\n    println!("Hello, World!");\n}',
        "widgets": {
            "Function": 'fn my_function() {\n    println!("This is a function");\n}',
            "Loop": 'for i in 1..5 {\n    println!("{}", i);\n}',
            "Struct": "struct Person {\n    name: String,\n    age: u32,\n}",
            "Enum": "enum Day { Monday, Tuesday, Wednesday }",
            "Condition": 'if x > 10 {\n    println!("Greater");\n} else {\n    println!("Smaller");\n}',
            "File Handling": 'use std::fs::File;\nlet file = File::create("output.txt");',
        },
    },
    "Java": {
        "base": '# Java Template\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
        "widgets": {
            "Function": 'public void myFunction() {\n    System.out.println("This is a function");\n}',
            "Array": "int[] arr = {1, 2, 3, 4};",
            "Loop": "for (int i = 0; i < 5; i++) {\n    System.out.println(i);\n}",
            "Condition": 'if (x > 10) {\n    System.out.println("Greater");\n} else {\n    System.out.println("Smaller");\n}',
            "Class": "class Person {\n    String name;\n    int age;\n}",
            "File Handling": 'import java.io.File;\nFile file = new File("test.txt");',
        },
    },
    "Python": {
        "base": "# Python Template\nprint('Hello, World!')\n",
        "widgets": {
            "Function": "def my_function():\n    print('This is a function')\n",
            "List": "my_list = [1, 2, 3, 4]",
            "Dictionary": "my_dict = {'name': 'John', 'age': 30}",
            "Loop": "for i in range(5):\n    print(i)",
            "Condition": "if x > 10:\n    print('Greater')\nelse:\n    print('Smaller')",
            "File Handling": "with open('test.txt', 'w') as f:\n    f.write('Hello, World!')",
        },
    },
    "C#": {
        "base": '# C# Template\nusing System;\npublic class Program {\n    public static void Main() {\n        Console.WriteLine("Hello, World!");\n    }\n}',
        "widgets": {
            "Function": 'public void MyFunction() {\n    Console.WriteLine("This is a function");\n}',
            "Array": "int[] arr = {1, 2, 3, 4};",
            "Loop": "for (int i = 0; i < 5; i++) {\n    Console.WriteLine(i);\n}",
            "Condition": 'if (x > 10) {\n    Console.WriteLine("Greater");\n} else {\n    Console.WriteLine("Smaller");\n}',
            "Class": "class Person {\n    public string Name;\n    public int Age;\n}",
            "File Handling": 'using System.IO;\nFile.WriteAllText("test.txt", "Hello, World!");',
        },
    },
    "C++": {
        "base": '# C++ Template\n#include <iostream>\nusing namespace std;\nint main() {\n    cout << "Hello, World!" << endl;\n    return 0;\n}',
        "widgets": {
            "Function": 'void myFunction() {\n    cout << "This is a function" << endl;\n}',
            "Array": "int arr[] = {1, 2, 3, 4};",
            "Loop": "for (int i = 0; i < 5; i++) {\n    cout << i << endl;\n}",
            "Condition": 'if (x > 10) {\n    cout << "Greater" << endl;\n} else {\n    cout << "Smaller" << endl;\n}',
            "Class": "class Person {\n    string name;\n    int age;\n};",
            "File Handling": '#include <fstream>\nofstream outfile;\noutfile.open("test.txt");\noutfile << "Hello, World!";\noutfile.close();',
        },
    },
    "JavaScript": {
        "base": "# JavaScript Template\nconsole.log('Hello, World!');\n",
        "widgets": {
            "Function": "function myFunction() {\n    console.log('This is a function');\n}",
            "Array": "let arr = [1, 2, 3, 4];",
            "Loop": "for (let i = 0; i < 5; i++) {\n    console.log(i);\n}",
            "Condition": "if (x > 10) {\n    console.log('Greater');\n} else {\n    console.log('Smaller');\n}",
            "Class": "class Person {\n    constructor(name, age) {\n        this.name = name;\n        this.age = age;\n    }\n}",
            "File Handling": "const fs = require('fs');\nfs.writeFileSync('test.txt', 'Hello, World!');",
        },
    },
    "Kotlin": {
        "base": '# Kotlin Template\nfun main() {\n    println("Hello, World!")\n}',
        "widgets": {
            "Function": 'fun myFunction() {\n    println("This is a function")\n}',
            "Array": "val arr = arrayOf(1, 2, 3, 4)",
            "Loop": "for (i in 1..5) {\n    println(i)\n}",
            "Condition": 'if (x > 10) {\n    println("Greater")\n} else {\n    println("Smaller")\n}',
            "Class": "class Person(val name: String, val age: Int)",
            "File Handling": 'import java.io.File;\nval file = File("test.txt");\nfile.writeText("Hello, World!")',
        },
    },
    "SQL": {
        "base": "# SQL Template\nSELECT 'Hello, World!';\n",
        "widgets": {
            "Create Table": "CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(100), age INT);",
            "Insert Data": "INSERT INTO users (name, age) VALUES ('John', 30);",
            "Select Data": "SELECT * FROM users WHERE name = 'John';",
            "Update Data": "UPDATE users SET age = 31 WHERE name = 'John';",
            "Delete Data": "DELETE FROM users WHERE name = 'John';",
            "Join Tables": "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id;",
        },
    },
    "Swift": {
        "base": '# Swift Template\nprint("Hello, World!")\n',
        "widgets": {
            "Function": 'func myFunction() {\n    print("This is a function")\n}',
            "Array": "let arr = [1, 2, 3, 4]",
            "Loop": "for i in 1...5 {\n    print(i)\n}",
            "Condition": 'if x > 10 {\n    print("Greater")\n} else {\n    print("Smaller")\n}',
            "Class": "class Person {\n    var name: String\n    var age: Int\n}",
            "File Handling": 'import Foundation\nlet file = FileManager.default.createFile(atPath: "test.txt", contents: "Hello, World!".data(using: .utf8), attributes: nil)',
        },
    },
    "TypeScript": {
        "base": "# TypeScript Template\nconsole.log('Hello, World!');\n",
        "widgets": {
            "Function": "function myFunction(): void {\n    console.log('This is a function');\n}",
            "Array": "let arr: number[] = [1, 2, 3, 4];",
            "Loop": "for (let i = 0; i < 5; i++) {\n    console.log(i);\n}",
            "Condition": "if (x > 10) {\n    console.log('Greater');\n} else {\n    console.log('Smaller');\n}",
            "Class": "class Person {\n    name: string;\n    age: number;\n    constructor(name: string, age: number) {\n        this.name = name;\n        this.age = age;\n    }\n}",
            "File Handling": "import * as fs from 'fs';\nfs.writeFileSync('test.txt', 'Hello, World!');",
        },
    },
    "HTML": {
        "base": '<!-- HTML Template -->\n<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Hello, World!</title>\n</head>\n<body>\n    <h1>Hello, World!</h1>\n</body>\n</html>',
        "widgets": {
            "Button": "<button>Click Me</button>",
            "Image": '<img src="image.jpg" alt="Image Description">',
            "Form": '<form><label for="name">Name:</label><input type="text" id="name"><input type="submit"></form>',
            "Link": '<a href="https://www.example.com">Visit Example</a>',
            "Table": "<table><tr><th>Header</th></tr><tr><td>Row 1</td></tr></table>",
            "List": "<ul><li>Item 1</li><li>Item 2</li></ul>",
        },
    },
}


class TemplateCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("Expanded Template Creator")
        self.root.geometry("700x500")
        self.root.configure(bg="#1E1E1E")

        # Title Label
        title_label = tk.Label(
            root,
            text="Select Technology and Widgets to Generate a Template",
            bg="#1E1E1E",
            fg="white",
            font=("Arial", 14, "bold"),
        )
        title_label.pack(pady=10)

        # Dropdown for technology selection
        self.tech_var = tk.StringVar()
        self.tech_dropdown = ttk.Combobox(
            root,
            textvariable=self.tech_var,
            values=list(TEMPLATES_WITH_WIDGETS.keys()),
            state="readonly",
            width=50,
        )
        self.tech_dropdown.pack(pady=10)
        self.tech_dropdown.set("Select a Technology")
        self.tech_dropdown.bind("<<ComboboxSelected>>", self.load_widgets)

        # Widgets selection area
        self.widgets_frame = tk.Frame(root, bg="#1E1E1E")
        self.widgets_frame.pack(pady=10, fill="both", expand=True)

        self.widgets_vars = {}

        # Folder selection button
        select_folder_button = tk.Button(
            root,
            text="Select Output Folder",
            command=self.select_output_folder,
            bg="white",
            fg="black",
            borderwidth=2,
            relief="groove",
        )
        select_folder_button.pack(pady=10)

        # Create template button
        create_button = tk.Button(
            root,
            text="Create Template",
            command=self.create_template,
            bg="white",
            fg="black",
            borderwidth=2,
            relief="groove",
        )
        create_button.pack(pady=10)

        # Selected folder label
        self.selected_folder = tk.StringVar()
        self.selected_folder.set("No folder selected.")
        folder_label = tk.Label(
            root,
            textvariable=self.selected_folder,
            bg="#1E1E1E",
            fg="white",
            wraplength=600,
        )
        folder_label.pack(pady=10)

        # Output message
        self.message_label = tk.Label(
            root, text="", bg="#1E1E1E", fg="white", wraplength=600
        )
        self.message_label.pack(pady=10)

    def select_output_folder(self):
        """Open a dialog to select the output folder."""
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder.set(folder)
            self.message_label.config(text="Selected folder: " + folder, fg="lightblue")

    def load_widgets(self, event=None):
        """Load available widgets for the selected technology."""
        tech = self.tech_var.get()
        self.widgets_vars.clear()
        for widget in self.widgets_frame.winfo_children():
            widget.destroy()

        if tech in TEMPLATES_WITH_WIDGETS:
            widgets = TEMPLATES_WITH_WIDGETS[tech]["widgets"]
            tk.Label(
                self.widgets_frame,
                text="Select Widgets:",
                bg="#1E1E1E",
                fg="white",
                font=("Arial", 12),
            ).pack(anchor="w", pady=5)
            for widget_name, _ in widgets.items():
                var = tk.BooleanVar()
                tk.Checkbutton(
                    self.widgets_frame,
                    text=widget_name,
                    variable=var,
                    bg="#1E1E1E",
                    fg="white",
                    selectcolor="#1E1E1E",
                ).pack(anchor="w")
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
                template_content += (
                    "\n" + TEMPLATES_WITH_WIDGETS[tech]["widgets"][widget]
                )

            # Save the file
            file_name = f"{tech.lower().replace(' ', '_')}_template"
            extension = {
                "Python": "py",
                "HTML": "html",
                "CSS": "css",
                "JavaScript": "js",
            }.get(tech, "txt")
            file_path = os.path.join(folder, f"{file_name}.{extension}")
            with open(file_path, "w") as file:
                file.write(template_content)

            self.message_label.config(text=f"Template created: {file_path}", fg="green")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create template: {e}")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TemplateCreator(root)
    root.mainloop()
