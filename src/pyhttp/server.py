# Socket setup, listening, accepting connections

from socket import *
from pyhttp.response import create_response

SERVER_HOST = 'localhost'
SERVER_PORT = 8080

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

print(f"Server is listening on port {SERVER_PORT}...")

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1500).decode()
    print(request)

    headers = request.split("\n")

    first_method_components = headers[0].split()

    http_method = first_method_components[0]
    path = first_method_components[1]

    response = create_response(http_method, path)

    client_socket.sendall(response.encode())
    client_socket.close()