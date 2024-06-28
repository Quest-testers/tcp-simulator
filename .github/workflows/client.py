import socket 

def tcp_client():
    host = '15.206.164.216'
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = 'Hello, Server!'
    client_socket.sendall(message.encode('utf-8'))

    data = client_socket.recv(5000)
    print('Received from server:', data.decode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    tcp_client()
