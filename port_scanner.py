import socket
import sys
from datetime import datetime

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except Exception:
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 port_scanner.py <target_ip>")
        sys.exit(1)
    
    target = sys.argv[1]
    print(f"Scanning {target} started at {datetime.now()}")
    
    common_ports = [21, 22, 23, 80, 443, 445, 3389]
    for port in common_ports:
        if scan_port(target, port):
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
    
    print("Scan completed.")

if __name__ == "__main__":
    main()
