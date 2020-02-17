import socket


def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    conn, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    # accept messages from client
    data_from_client = conn.recv(100)
    decoded_data = data_from_client.decode('utf-8')
    print("[S]: Data received from client: {}".format(decoded_data))
    with open('out-proj0.txt', 'a') as outfile:
        outfile.write(decoded_data[::-1])

    # reverse the message received from client and send back
    msg = 'Finished recording message from client.'
    conn.send(msg.encode('utf-8'))
    conn.close()

    # Close the server socket
    ss.close()
    exit()
