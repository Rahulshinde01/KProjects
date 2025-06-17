import subprocess
import sys

def ping_host(host):
    try:
        # Command to ping the host (Linux/macOS compatible, -n 4 for Windows)
        # For cross-platform, you might need to check sys.platform
        if sys.platform.startswith('win'):
            command = ["ping", "-n", "4", host]
        else:
            command = ["ping", "-c", "4", host]

        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print("Error:", result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error pinging {host}: {e}")
        print("Standard Output:", e.stdout)
        print("Standard Error:", e.stderr)
        return False
    except FileNotFoundError:
        print(f"Error: 'ping' command not found. Make sure it's in your PATH.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ping_python.py <hostname_or_ip>")
        sys.exit(1)
    
    target_host = sys.argv[1]
    print(f"Pinging {target_host} with Python...")
    ping_host(target_host) 