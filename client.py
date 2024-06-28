import socket

HOST = '15.206.164.216'  # Replace with your EC2 instance's public IP
PORT = 5001                  # Port on which the server is listening

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, TCP Server!')
    data = s.recv(1024)

print('Received', repr(data))


