import socket
import sys

def start_traffic_simulation():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <IP> <PORT>")
        sys.exit(1)

    target_ip = sys.argv[1]
    try:
        target_port = int(sys.argv[2])
    except ValueError:
        print("[-] Error: Port must be an integer.")
        sys.exit(1)

    print(f"Connecting to {target_ip}:{target_port}...")
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))

        
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_traffic_simulation()
