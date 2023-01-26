import socket

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():
    # create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 12345)) # bind to port 12345

    while True:
        # receive temperature in Fahrenheit from client
        data, addr = sock.recvfrom(1024)
        fahrenheit = float(data.decode())

        # convert temperature to Celsius
        celsius = fahrenheit_to_celsius(fahrenheit)

        # send Celsius temperature back to client
        sock.sendto(str(celsius).encode(), addr)

        print(f'Converted {fahrenheit} F to {celsius} C and sent to {addr}')

if __name__ == '__main__':
    main()
