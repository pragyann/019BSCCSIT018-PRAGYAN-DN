import socket
import time

def handle_request(request):
    if request == "time":
        return time.ctime()
    elif request.startswith("echo"):
        return request[len("echo")+1:]
    else:
        return "Invalid request"

def main():
    # Server configuration
    host = '127.0.0.1'
    port = 12345

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print("Server listening on {}:{}".format(host, port))

    while True:
        # Accept incoming connection
        client_socket, addr = server_socket.accept()
        print("Connection from:", addr)

        # Receive request from client
        request = client_socket.recv(1024).decode()
        print("Received:", request)

        # Process request and generate response
        response = handle_request(request)

        # Send response back to client
        client_socket.sendall(response.encode())

        # Close connection
        client_socket.close()

if __name__ == "__main__":
    main()
