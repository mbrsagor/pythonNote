import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8888)
server_socket.bind(server_address)

# Listen for incoming connections (max 5 connections in the queue)
server_socket.listen(5)
print("Server listening on {}:{}".format(*server_address))

while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from {}:{}".format(*client_address))

    # Send a welcome message to the client
    message = "Welcome to the server!"
    client_socket.send(message.encode('utf-8'))

    # Close the connection
    client_socket.close()
