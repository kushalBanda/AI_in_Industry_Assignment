import socket

def main():
    server_ip = "192.168.1.4" 
    server_port = 12345   

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print("Server listening on {}:{}".format(server_ip, server_port))

    client_socket, client_address = server_socket.accept()
    print("Connection established with client:", client_address)

    while True:
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break
        print("Received from client:", data)

        response = "Server received: " + data
        client_socket.send(response.encode("utf-8"))

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
