# Client.py

import socket

def main():
    server_ip = "192.168.1.4" 
    server_port = 12345           

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    message = input("Enter a message to send to the server: ")
    client_socket.send(message.encode("utf-8"))

    response = client_socket.recv(1024).decode("utf-8")
    print("Received from server:", response)

    client_socket.close()

if __name__ == "__main__":
    main()
