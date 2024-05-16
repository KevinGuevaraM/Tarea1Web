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
            connection.sendall(f'{"A"}'.encode())
            time.sleep(0.1)
            # Consiga la información que le enviaron
            if connection:
                data = connection.recv(1024)
                connection.close()
                data = data.decode()
                # Deserialice la información
                data = data.split(";")
                print("CONSUMER:       id: " + data[0])
                print("CONSUMER:       Tiempo de creación: " + data[1])

                print("\nCONSUMER:       Header: ")
                headerParts = data[2].split(",")
                for part in headerParts:
                    print("CONSUMER:       " + part)
                
                print("\nCONSUMER:       Body: ")
                bodyParts = data[3].split(",")
                for part in bodyParts:
                    print("CONSUMER:       " + part)


                time.sleep(5)
        except ConnectionAbortedError:
            pass
            