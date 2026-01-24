# client.py

import socket

# create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client_socket.connect(("127.0.0.1", 5005))

# receive data
data = client_socket.recv(1024)
print("Received:", data.decode())

# close connection
client_socket.close()