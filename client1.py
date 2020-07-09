import socket
def client_program():
 host = socket.gethostname()  # The server's hostname or IP address
 port = 55555        # The port used by the server
 client_socket=socket.socket()
 client_socket.connect((host, port))
 
    
 client_socket.send(b'Hello, world')
 data = client_socket.recv(1024)

 print('Received', repr(data))

 client_socket.close()


if __name__ == '__main__':
    client_program()

