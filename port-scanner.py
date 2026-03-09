import socket

print("Simple Python Port Scanner")

target = input ("Enter target IP: ")

ports = [21, 22, 23, 53, 80, 110, 139, 143, 443, 445, 3389]

print(f"\nScanning target {target}...\n")

for port in ports:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target,port))

    if result == 0:
          print(f"Port {port} is OPEN")

s.close()
