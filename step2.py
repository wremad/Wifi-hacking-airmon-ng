"""
List of commands using in this tool 
ip addr 
iwconfig
sudo airmon-ng check kill
sudo airmon-ng start wlan0
iwconfig
sudo airodump-ng wlan0mon
sudo airodump-ng -w {file name} -c {channel no} --bssid {ssid} wlan0mon
new TAB :- sudo aireplay-ng --deauth 0 -a {ssid} wlan0mon
"""

import subprocess
import signal
import sys

def run_airodump():
    # Define the command to run airodump-ng
    command = 'sudo airodump-ng wlan0mon'

    # Execute the command in a new terminal window and handle interruptions
    try:
        # Run the command
        process = subprocess.Popen(command, shell=True)
        # Wait for the process to complete
        process.wait()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
        process.terminate()  # Terminate the subprocess
        process.wait()       # Wait for the subprocess to terminate

if __name__ == "__main__":
    run_airodump()