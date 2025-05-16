import socket

def send_print_job(printer_ip, printer_port, file_path):
    # Open the file to print
    try:
        with open(file_path, "rb") as file:
            data = file.read()

        # Connect to the printer over port 9100
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)  # Optional timeout for the socket connection
            s.connect((printer_ip, printer_port))  # Connect to printer's IP and port 9100
            s.sendall(data)  # Send the file data to the printer

        print(f"Print job sent to {printer_ip} on port {printer_port}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Prompt the user for the printer IP
printer_ip = input("Please enter the printer IP address: ")  # User input for printer IP
printer_port = 9100  # Default port for raw printing

# Hardcoded file path to the file you want to print
file_path = r"\\10.44.4.201\00_Misc\Test Files\3. PDF\(198)_Tauranga.pdf"


send_print_job(printer_ip, printer_port, file_path)
