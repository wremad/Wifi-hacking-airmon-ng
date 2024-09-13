import subprocess
import signal
import sys

def check_wlan0_interface():
    try:
        result = subprocess.run(['ip', 'addr'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        if 'wlan0' in result.stdout:
            print("'wlan0' interface is found.")
            return True
        else:
            print("'wlan0' interface is NOT found. Stopping here.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def check_wlan0_monitor_mode():
    try:
        result = subprocess.run(['iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        if any(iface for iface in result.stdout.splitlines() if 'Mode:Monitor' in iface):
            print("Wireless interface is in Monitor mode.")
            return True
        else:
            print("Wireless interface is not in Monitor mode.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def kill_conflicting_processes():
    try:
        result = subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        print("Processes killed by 'airmon-ng check kill':")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to kill conflicting processes: {e}")
        return False

def start_monitor_mode():
    try:
        result = subprocess.run(['sudo', 'airmon-ng', 'start', 'wlan0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Output of 'airmon-ng start wlan0':")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to start monitor mode: {e}")
        return False
# Call the function to check if wlan0 exists
if check_wlan0_interface():
    if kill_conflicting_processes():
        if start_monitor_mode():
            if check_wlan0_monitor_mode():
                print("Successfully switched 'wlan0' to monitor mode.")
            else:
                print("Failed to switch 'wlan0' to monitor mode. Exiting.")
        else:
            print("Failed to execute monitor mode setup. Exiting.")
    else:
        print("Failed to kill conflicting processes. Exiting.")
else:
    print("Exiting as 'wlan0' interface is not found.")