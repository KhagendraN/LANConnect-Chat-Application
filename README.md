# LAN Chat Application

A simple LAN-based chat application built with Python socket programming, allowing multiple users to communicate over a Local Area Network (LAN). This project demonstrates real-time data transfer and basic networking concepts using sockets.

## Features
- **Real-time Messaging**: Enables multiple clients to communicate in real-time.
- **Multi-client Support**: Each client runs in its own thread, allowing multiple users to connect simultaneously.
- **Exit Option**: Clients can type `exit` to leave the chat.
  
## Requirements
- Python 3.x
- Basic understanding of Python socket programming
- Local network setup for testing with multiple devices (or multiple terminals on the same device)

## Installation and Setup
1. **Clone this repository**:
    ```bash
    git clone https://github.com/KhagendraN/LANConnect-Chat-Application.git
    cd LANConnect-Chat-Application
    ```

2. **Run the Server**:
   - Open a terminal window and start the server:
     ```bash
     python server.py
     ```
   - This will start the server on `localhost` at the default port.

3. **Run the Clients**:
   - Open another terminal window and run:
     ```bash
     python client.py
     ```
   - You can open additional terminals and run `client.py` in each to simulate multiple clients.

4. **Connecting from Multiple Devices**:
   - If running across multiple devices on the same network, use the server's LAN IP instead of `localhost`.
   - Update `HOST` in both `server.py` and `client.py` files to match the server's IP address (e.g., `192.168.x.x`).
   - All clients should connect using this IP to join the same chat room.

## Usage
1. Type your message in any client terminal and press `Enter` to send.
2. All connected clients, except the sender, will see the message.
3. To exit the chat, type `exit` and press `Enter`.

## Code Overview

### server.py
This script initializes the server, handles incoming connections, and broadcasts messages to all connected clients.

- **`broadcast(message, _client_socket)`**: Sends the received message to all clients except the sender.
- **`handle_client(client_socket)`**: Receives and handles messages from a single client.
- **`start_server()`**: Sets up the server and listens for incoming connections.

### client.py
This script connects to the server, sends messages from the client, and displays incoming messages from other clients.

- **`receive_messages(client_socket)`**: Continuously listens for messages from the server and displays them.
- **`main()`**: Connects to the server and starts sending/receiving messages.

## Example Output

### Server
```plaintext
Server is running and waiting for connections...
Connected to ('192.168.254.6', 45382)
Connected to ('192.168.254.6', 59526)
