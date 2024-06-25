import socket 

def start_client(host, port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'Hello, server')
        data = s.recv(1032)
        print(f'Received {data.decode()}')

if __name__ == "__main__":
    start_client('15.206.164.216')