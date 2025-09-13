import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221))
    try:
        while True:
            client_socket, _ = server_socket.accept()
            print("Socket accepted a connection!")
            data = client_socket.recv(1024)
            request = data.decode()
            print(request)
            if request.startswith("GET / HTTP/1.1"):
                response = "HTTP/1.1 200 OK\r\n\r\n"
            else:
                response = "HTTP/1.1 404 Not Found\r\n\r\n"
            client_socket.sendall(response.encode())
    except KeyboardInterrupt:
        print("KeyboardInterrupt received, exiting.")
        pass
    finally:
        server_socket.close()   

if __name__ == "__main__":
    main()
