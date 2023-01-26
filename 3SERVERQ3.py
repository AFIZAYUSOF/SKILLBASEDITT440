import socket
import threading
import random

quotes = ["Jika Anda ingin bercinta, pergilah ke perguruan tinggi. Jika Anda ingin pendidikan, pergilah ke perpustakaan.",
          "Lebih baik terjebak di perpustakaan bersama kamu daripada merasa sendirian di kantin.",
          "Perpustakaan adalah tempat untuk memenuhi dahaga ilmu pengetahuan.",
          "Jika kebenaran adalah kecantikan, kenapa tidak ada orang yang merapikan rambut mereka di perpustakaan?",
          "Saya jatuh cinta dengan membaca apabila saya dibenarkan memilih apa sahaja buku yang saya ingin semak keluar dari perpustakaan."]

def handle_client(client_sock):
    """
    Handles a single client request by sending a randomized quote.
    """
    rand_quote = random.choice(quotes)
    client_sock.sendall(rand_quote.encode())
    client_sock.close()

def main():
    """
    The main function that creates a TCP socket and listens for client connections.
    """
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('', 8888))
    server_sock.listen(5)

    while True:
        client_sock, _ = server_sock.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_sock,))
        client_thread.start()

if __name__ == '__main__':
    main()
