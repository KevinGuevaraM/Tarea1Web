import time
import socket


HOST = "127.0.0.1" # Esto es local :B
PORT = 1800 # Puerto al que escucha
BROKERPORT = 1789 # Puerto del broker


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024)
    s.bind((HOST, PORT))
    s.listen()
    while True:
        try:
            connection, addr = s.accept()
            # Haga que ÉL envíe el primer mensaje (Esto porque hay una cola interna en cada socket, es rarísimo)
            connection.sendall(f'{"A"}'.encode())
            # Consiga la información que le enviaron
            if connection:
                data = connection.recv(1024)
                connection.close()
                data = data.decode()
                # Haga lo que quiera con esa información acá, ya la tiene.
                
        except ConnectionAbortedError:
            # Esto es necesario.
            pass
            