# server.py
import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())  # Server IP address
PORT = 5050      # Server port

# List to keep track of all connected clients
clients = []

def broadcast(message, _client_socket):
    """Send a message to all connected clients."""
    for client in clients:
        if client != _client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    """Handle incoming messages from a specific client."""
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server():
    """Initialize the server and accept connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Server is running and waiting for connections...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connected to {address}")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
