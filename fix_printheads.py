import subprocess
import json
import time

# Load configuration from config.json
def load_config():
    config_path = r"C:\Users\jingheng.wong\Desktop\Automation_smoke_test\Configuration\config.json"
    with open(config_path, "r") as config_file:
        return json.load(config_file)

# Function to establish SSH connection, login to maia, and run a list of commands
def connect_to_maia():
    config = load_config()
    root_host = config["host"]["hostname"]  # Root host
    root_user = "root"  # Username for root
    root_password = "myroot"  # Password for root

    # List of commands to send
    commands = [
        "Pen0 clearErrors",
        "Pen0 acceptPen",
        "Pen1 clearErrors",
        "Pen1 acceptPen",
        "Pen2 clearErrors",
        "Pen2 acceptPen",
        "Pen3 clearErrors",
        "Pen3 acceptPen",
        "Pen4 clearErrors",
        "Pen4 acceptPen",
        "Pen5 clearErrors",
        "Pen5 acceptPen"
    ]

    try:
        # Step 1: SSH into the root host
        print(f"Connecting to {root_host} as {root_user}...")
        plink_command = f'plink.exe -ssh {root_user}@{root_host} -pw {root_password}'

        # Start the SSH connection to the root host
        process = subprocess.Popen(plink_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Step 2: After logging in as root, connect to maia
        print(f"Logging into maia...")
        process.stdin.write("ssh 156.152.91.2\n")  # Directly SSH into maia with its IP
        process.stdin.flush()  # Ensure the command is sent to the remote machine

        # Wait for maia prompt (adjust time if necessary)
        time.sleep(3)
        process.stdout.readline()  # Read output to ensure login happens
        process.stdin.write("tl\n")
        process.stdin.flush()

        time.sleep(3)

        # Step 3: Iterate over the list of commands and send each one
        for command in commands:
            print(f"Sending command: {command}")
            process.stdin.write(f"{command}\n")  # Send the current command to the remote session
            process.stdin.flush()  # Ensure the command is sent to the remote machine

        # Step 4: Capture and display the output in real-time
        for line in process.stdout:
            print(line, end='')  # Print the output from the commands

        # Capture any errors
        for line in process.stderr:
            print(line, end='')  # Print any errors if they occur

        # Wait for the process to complete
        process.wait()

    except subprocess.CalledProcessError as e:
        print(f"Error during SSH connection or entering commands: {e}")

# Main entry point for the script
if __name__ == "__main__":
    connect_to_maia()
