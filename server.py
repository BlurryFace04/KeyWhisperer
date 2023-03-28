import socket
import sys


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print("Error getting host IP address:", e)
        return None


def handle_client(client_socket):
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received data: {data.decode('utf-8')}")
    except Exception as e:
        print(f"Client disconnected: {e}")
    finally:
        client_socket.close()


def main():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the SO_REUSEADDR socket option
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the address and port
    try:
        s.bind(('0.0.0.0', 12345))
    except socket.error as e:
        print(f"Bind failed: {e}")
        sys.exit()

    host_ip = get_host_ip()
    if host_ip:
        print(f"Host IP address: {host_ip}")

    # Listen for incoming connections
    s.listen(1)
    print("Listening for incoming connections...")
    while True:
        try:
            # Accept the connection
            conn, addr = s.accept()
            print(f"Connected with {addr[0]}:{addr[1]}")

            # Handle the client connection
            handle_client(conn)
        except Exception as e:
            print(f"Error while handling connection: {e}")

    # Close the server socket
    s.close()


if __name__ == "__main__":
    main()
