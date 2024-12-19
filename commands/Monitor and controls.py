import tkinter as tk
from tkinter import messagebox
import serial
import serial.tools.list_ports
import threading
import pyautogui
import keyboard


class PortMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Port Monitor App")
        self.root.geometry("800x600")  # Initial size
        self.root.config(bg="#F7F7F7")

        # Create a canvas for the entire scrollable content
        self.canvas = tk.Canvas(self.root, bg="#F7F7F7")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for the canvas (only one scrollbar for the whole app)
        self.scrollbar = tk.Scrollbar(
            self.root, orient="vertical", command=self.canvas.yview
        )
        self.scrollbar.pack(side=tk.RIGHT, fill="y")

        # Create a frame to hold all UI elements inside the canvas
        self.frame = tk.Frame(
            self.canvas, bg="#F7F7F7", width=1200
        )  # Width is large for horizontal expansion
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.canvas.config(yscrollcommand=self.scrollbar.set)

        self.label = tk.Label(
            self.frame,
            text="Monitor and Control Serial Ports",
            font=("Arial", 16, "bold"),
            fg="#4A90E2",
            bg="#F7F7F7",
        )
        self.label.grid(row=0, column=0, pady=10, sticky="w", columnspan=2)

        # Frame for monitor display, taking the left 2/3 of the width
        monitor_frame = tk.Frame(self.frame, bg="#F7F7F7")
        monitor_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        # Monitor display (large area)
        self.monitor_canvas = tk.Canvas(monitor_frame, bg="#1E1E1E", bd=2)
        self.monitor_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Frame to hold monitor text
        self.monitor_display_frame = tk.Frame(self.monitor_canvas, bg="#1E1E1E")
        self.monitor_canvas.create_window(
            (0, 0), window=self.monitor_display_frame, anchor="nw"
        )

        self.monitor_display = tk.Label(
            self.monitor_display_frame,
            text="",
            font=("Courier New", 12),
            fg="#FFFFFF",
            bg="#1E1E1E",
            anchor="nw",
            justify="left",
        )
        self.monitor_display.grid(row=0, column=0, padx=10, pady=5)

        # Frame for the devices list, placed below the monitor
        device_frame = tk.Frame(self.frame, bg="#F7F7F7")
        device_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        # Display devices list (taking 2/3 width of the app)
        self.port_listbox = tk.Listbox(
            device_frame,
            width=40,
            height=8,
            font=("Arial", 12),
            bg="#FFFFFF",
            fg="#000000",
            bd=2,
        )
        self.port_listbox.grid(row=0, column=0, padx=10, sticky="w")

        # Frame for the buttons (taking 1/3 of the width)
        button_frame = tk.Frame(self.frame, bg="#F7F7F7")
        button_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Buttons for device control
        self.select_button = tk.Button(
            button_frame,
            text="Select",
            command=self.select_device,
            font=("Arial", 12),
            bg="#4A90E2",
            fg="#FFFFFF",
            relief="flat",
        )
        self.select_button.grid(row=0, column=0, pady=10, sticky="ew")

        self.connect_button = tk.Button(
            button_frame,
            text="Connect",
            command=self.connect_and_monitor,
            font=("Arial", 12),
            bg="#4A90E2",
            fg="#FFFFFF",
            relief="flat",
        )
        self.connect_button.grid(row=1, column=0, pady=10, sticky="ew")

        self.refresh_button = tk.Button(
            button_frame,
            text="Refresh Ports",
            command=self.refresh_ports,
            font=("Arial", 12),
            bg="#4A90E2",
            fg="#FFFFFF",
            relief="flat",
        )
        self.refresh_button.grid(row=2, column=0, pady=10, sticky="ew")

        self.serial_connection = None
        self.selected_device = None

        self.refresh_ports()

        # Update the canvas scroll region whenever the frame is resized
        self.frame.bind("<Configure>", self.on_frame_resize)

    def on_frame_resize(self, event):
        """Update the scroll region when the frame size changes"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def refresh_ports(self):
        """Refresh the list of available serial ports"""
        self.port_listbox.delete(0, tk.END)
        ports = self.get_serial_ports()
        if ports:
            for port in ports:
                self.port_listbox.insert(tk.END, port)
        else:
            self.port_listbox.insert(tk.END, "No ports available")

    def get_serial_ports(self):
        """Get a list of available serial ports with more details"""
        ports = []
        for port in serial.tools.list_ports.comports():
            port_info = f"{port.device} ({port.description})"
            ports.append(port_info)
        return ports

    def select_device(self):
        """Select a device from the list and highlight it"""
        selected_index = self.port_listbox.curselection()
        if selected_index:
            selected_device = self.port_listbox.get(selected_index[0])
            if self.selected_device:
                # Reset the previous selection highlight to red
                self.port_listbox.itemconfig(self.selected_device, {"bg": "red"})
            # Highlight the new selected device in green
            self.port_listbox.itemconfig(selected_index[0], {"bg": "green"})
            self.selected_device = selected_index[0]
            # Update connect button
            self.connect_button.config(text="Connect")
        else:
            messagebox.showwarning("No Device Selected", "Please select a device.")

    def connect_and_monitor(self):
        """Connect to the selected port and start monitoring"""
        if not self.selected_device:
            messagebox.showwarning(
                "No Device Selected", "Please select a port to connect."
            )
            return

        selected_port = self.port_listbox.get(self.selected_device)
        port_name = selected_port.split(" ")[
            0
        ]  # Extract the port name (e.g., COM1 or /dev/ttyUSB0)
        try:
            # Check if already connected
            if self.serial_connection:
                messagebox.showinfo(
                    "Reconnected",
                    f"Already connected to {port_name}. Monitoring data...",
                )
                return

            self.serial_connection = serial.Serial(port_name, 9600, timeout=1)
            messagebox.showinfo(
                "Connected", f"Connected to {port_name}. Monitoring data..."
            )
            self.connect_button.config(
                text="Reconnect"
            )  # Change button text to Reconnect
            threading.Thread(target=self.monitor_data, daemon=True).start()
            threading.Thread(target=self.capture_input, daemon=True).start()

        except serial.SerialException as e:
            messagebox.showerror("Error", f"Could not connect to port {port_name}: {e}")

    def monitor_data(self):
        """Monitor incoming data from the connected device"""
        while True:
            if self.serial_connection and self.serial_connection.in_waiting > 0:
                data = self.serial_connection.readline().decode("utf-8").strip()
                self.display_data(data)

    def display_data(self, data):
        """Update the monitor display with new data"""
        self.monitor_display.config(
            text=self.monitor_display.cget("text") + data + "\n"
        )
        self.monitor_display_frame.update_idletasks()
        self.monitor_display_frame.update()

    def capture_input(self):
        """Capture keyboard and mouse input and send to the device via serial"""
        while True:
            # Check for keyboard events and send the key pressed to the serial device
            if keyboard.is_pressed():
                key = keyboard.read_event(suppress=True).name
                if self.serial_connection:
                    self.serial_connection.write(f"KEY:{key}\n".encode())

            # Check for mouse events
            x, y = pyautogui.position()
            if self.serial_connection:
                self.serial_connection.write(f"MOUSE:{x},{y}\n".encode())


if __name__ == "__main__":
    root = tk.Tk()
    app = PortMonitorApp(root)
    root.mainloop()
