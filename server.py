### server.py
import socket

# create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind to IP and port
server_socket.bind(("127.0.0.1", 5005))

# listen for connections
server_socket.listen(1)
print("Server is listening...")

# accept client connection
conn, addr = server_socket.accept()
print("Connected by", addr)

# send data to client
conn.sendall(b"Hello from server")

# close connection
conn.close()
server_socket.close()