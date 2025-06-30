Simple Port Scanner
A simple Python script for beginners to scan common ports on a target system. It checks if ports like 80 (web) or 22 (SSH) are open.
Why This Project?

Learn basic cybersecurity skills (port scanning).
Safe for testing in a lab (e.g., with Metasploitable VM).
Easy to understand and build upon.

What You Need

Kali Linux (or any Linux with Python 3)
Python 3 (install with sudo apt install python3)
A test system like Metasploitable VM

How to Install

Get the project from GitHub:
git clone https://github.com/NitingautamEO/port-scanner.git
cd port-scanner


Make sure Python 3 is installed:
sudo apt install python3



How to Use
Run the script with a target IP:
python3 port_scanner.py <target_ip>

Example:
python3 port_scanner.py 192.168.56.101

Example Result
Scanning 192.168.56.101 started at 2025-07-01 12:00:00
Port 21 is OPEN
Port 22 is OPEN
Port 23 is OPEN
Port 80 is OPEN
Port 443 is CLOSED
Port 445 is OPEN
Port 3389 is CLOSED
Scan completed.

Important

Only scan systems you own or have permission to test (like Metasploitable).
This is for learning and ethical hacking only.

License
MIT License
