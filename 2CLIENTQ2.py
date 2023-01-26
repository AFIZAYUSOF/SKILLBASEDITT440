    # send temperature to server
    sock.sendto(str(fahrenheit).encode(), ('127.0.0.1', 12345))

    # receive temperature in Celsius from server
    data, _ = sock.recvfrom(1024)
    celsius = float(data.decode())

    # display temperature in Celsius
    print(f'Temperature in Celsius: {celsius}')

if __name__ == '__main__':
    main()
