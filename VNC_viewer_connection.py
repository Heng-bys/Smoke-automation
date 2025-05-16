import subprocess
import json
import threading


def read_output(stream, prefix=''):
    """Read lines from a stream and print them with an optional prefix."""
    for line in iter(stream.readline, ''):
        if line:
            print(f"{prefix}{line}", end='')


def load_config():
    config_path = r"C:\Users\jingheng.wong\Desktop\Automation_smoke_test\Configuration\config.json"
    with open(config_path, "r") as config_file:
        return json.load(config_file)


def connect_vnc():
    config = load_config()
    hostname = config["host"]["hostname"]
    username = config["host"]["username"]
    password = config["host"]["password"]

    # Start SSH connection
    plink_command = f'plink.exe -ssh {username}@{hostname} -pw {password}'

    try:
        process = subprocess.Popen(
            plink_command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1  # Line buffered
        )

        # Start threads to read output and errors concurrently
        stdout_thread = threading.Thread(target=read_output, args=(process.stdout, ''))
        stderr_thread = threading.Thread(target=read_output, args=(process.stderr, 'ERROR: '))

        stdout_thread.daemon = True
        stderr_thread.daemon = True

        stdout_thread.start()
        stderr_thread.start()

        # Send the X11VNC command
        process.stdin.write("x11vnc\n")
        process.stdin.flush()

        # Wait for the process to complete
        process.wait()

        # Wait for output threads to finish
        stdout_thread.join()
        stderr_thread.join()

    except Exception as e:
        print(f"Error during SSH connection or starting X11VNC: {e}")


if __name__ == "__main__":
    connect_vnc()