import socket

def main():
    # Server configuration
    host = '127.0.0.1'
    port = 12345

    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        # Send request to server
        request = input("Enter your request ('time' or 'echo <message>'): ")
        client_socket.sendall(request.encode())

        # Receive response from server
        response = client_socket.recv(1024).decode()
        print("Response:", response)

if __name__ == "__main__":
    main()
