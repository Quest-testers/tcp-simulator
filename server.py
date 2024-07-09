import socket

import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5001       # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(5001)
            if not data:
                break
            conn.sendall(data)
