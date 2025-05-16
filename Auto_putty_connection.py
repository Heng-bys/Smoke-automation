import subprocess
import json


# Load configuration from config.json
def load_config():
    config_path = r"C:\Users\jingheng.wong\Desktop\Automation_smoke_test\Configuration\config.json"
    with open(config_path, "r") as config_file:
        return json.load(config_file)


# Function to connect to the host using Putty (Plink)
def connect_putty():
    config = load_config()
    hostname = config["host"]["hostname"]
    username = config["host"]["username"]
    password = config["host"]["password"]

    # Command to run Plink and establish the SSH connection
    plink_command = f'plink.exe -ssh {username}@{hostname} -pw {password}'

    try:
        subprocess.run(plink_command, shell=True, check=True)
        print(f"Connected to {hostname} successfully!")

    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to {hostname}: {e}")


# Main entry point for the script
if __name__ == "__main__":
    connect_putty()
