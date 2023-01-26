import socket

def main():
    """
    The main function that creates a TCP socket and connects to the server.
    """
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('127.0.0.1', 8888))
    data = client_sock.recv(1024)
    quote = data.decode()
    print("Today's Quote: " + quote)
    client_sock.close()

if __name__ == '__main__':
    main()
