# client.py
import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())  # Server IP address
PORT = 5050        # Server port

def receive_messages(client_socket):
    """Listen for incoming messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Disconnected from server")
            client_socket.close()
            break

def main():
    """Main client function."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Start a thread to listen for messages from the server
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    # Main loop to send messages
    while True:
        message = input()
        if message.lower() == 'exit':
            client_socket.close()
            break
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
