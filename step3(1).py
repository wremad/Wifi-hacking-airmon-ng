import subprocess
import sys

def get_user_input():
    file_name = input("Enter the file name (including path) for output (e.g., /path/to/file): ")
    channel_no = input("Enter the channel number: ")
    ssid = input("Enter the BSSID (or leave blank to capture all): ")
    return file_name, channel_no, ssid

def run_custom_airodump(file_name, channel_no, ssid):
    try:
        # Construct the command in one line
        command = f"sudo airodump-ng -w {file_name} -c {channel_no}"
        if ssid:  # Add --bssid only if it is provided
            command += f" --bssid {ssid}"
        command += " wlan0mon"

        # Print the constructed command for verification
        print(f"Running custom airodump-ng command: {command}")
        
        # Run the command in a shell and display output in real-time
        process = subprocess.Popen(command, shell=True, text=True)
        
        # Wait for the process to complete
        try:
            process.wait()
        except KeyboardInterrupt:
            print("\nInterrupted by user.")
            process.terminate()
            process.wait()
            print("Custom airodump-ng process terminated.")

    except subprocess.CalledProcessError as e:
        print(f"Failed to run airodump-ng with custom parameters: {e}")

# Example usage
if __name__ == "__main__":
    file_name, channel_no, ssid = get_user_input()
    run_custom_airodump(file_name, channel_no, ssid)