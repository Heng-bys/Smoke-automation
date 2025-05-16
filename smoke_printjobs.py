import socket
import os

def send_print_job(printer_ip, printer_port, file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file at {file_path} does not exist.")
        return

    try:
        # Open the file to print
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

# List of file paths for multiple print jobs
file_paths = [
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\tower_a1.rs",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\tower_a1_3pages.rs",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\A4.urf",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\A0.urf",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\A3.urf",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\Letter.urf",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\DinA1_image_LocPort_Neptune_PCL3v4.prn",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\DinA0_vectorial_LocPort_Neptune_PCL3v4.prn",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\sRGB_A4_600dpi.jpg",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\A4_600dpi_sRGB.tif",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\Quick_Check_Niagara_x64_600dpi_v1.tif",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\onepage-letter-srgb-8-300dpi.pwg",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\Collate\A4_600dpi_sRGB_2JobCopies_UNCOLLATED.rs",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\Collate\A4_600dpi_sRGB_2JobCopies_COLLATED.rs",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\JobCopies\A4_600dpi_sRGB_2JobCopies.rs",
    r"C:\Users\jingheng.wong\Desktop\HPIO_job\PageCopies\A4_600dpi_sRGB_2CopiesOfSecondPage.rs"

]

# Loop through the file paths and send each print job
for file_path in file_paths:
    send_print_job(printer_ip, printer_port, file_path)
