import socket

# Input from user
host = input("Enter host (e.g., 127.0.0.1 or google.com): ")
port = int(input("Enter port number: "))

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

# Check port status
result = sock.connect_ex((host, port))

if result == 0:
    print(f"Port {port} is OPEN on {host}")
else:
    print(f"Port {port} is CLOSED on {host}")

sock.close()