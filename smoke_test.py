import tkinter as tk
from tkinter import messagebox
import subprocess

# Function to run the selected script
def run_script(script_file):
    try:
        # Run the selected script
        subprocess.run(script_file, shell=True, check=True)
        messagebox.showinfo("Success", f"{script_file} executed successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to execute {script_file}: {e}")

# Create the main window
root = tk.Tk()
root.title("Smoke Test Executor")

# Set window size
root.geometry("300x250")

# Create a label
label = tk.Label(root, text="Select a test to run", font=("Arial", 14))
label.pack(pady=20)

# Create buttons for each script
button_putty = tk.Button(root, text="Auto Putty Connection", width=25,
                         command=lambda: run_script(r"Auto_putty_connection.py"))
button_putty.pack(pady=5)

button_vnc = tk.Button(root, text="VNC Viewer Connection", width=25,
                       command=lambda: run_script(r"VNC_viewer_connection.py"))
button_vnc.pack(pady=5)

# Run the main event loop
root.mainloop()
