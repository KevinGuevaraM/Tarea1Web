from datetime import datetime
import socket
import uuid

HOST = "127.0.0.1"
PORT = 1799 # Puerto al que escucho
BROKERPORT = 1789 # Puerto del broker...
class Message:
    """!
    @brief Clase mensaje para la construcción de lo que se enviará


    """
    def __init__(self, header: dict = None, body: dict = None):
        """!
        @brief Iniciador del productor

        Parametros : 
            @param header = None => un diccionario para poner en el header
            @param body = None => un diccionario para poner en el body

        """
        #
        self.timestamp = datetime.now()
        #Qué es uuid? No sé, pero la tarea me dijo que lo pusiera y encontré esa documentación
        self.id = uuid.uuid4()

        if header == None:
            self.header = dict()
        else:
            self.header = header
        
        if body == None:
            self.body = dict()
        else:
            self.body = body
        

def enviar_request(host, port, peticion):
    """!
    @brief Función para enviar un mensaje al broker

    Paramètres : 
        @param host => host del broker
        @param port => puerto del broker
        @param peticion => mensaje para enviarle al broker

    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(peticion.encode())

        if int(s.recv(1024).decode()) == 1:
            print ("PRODUCER:       El mensaje se envió correctamente")
        else:
            print("PRODUCER:       El mensaje no se pudo enviar")


def main():
    # Ejemplo de serialización de un mensaje
    mensaje = Message({"De": "Pedrito", "Para": "Sepa Dios"}, {"Contenido": "Despacito 2 es mejor que despacito 1"})

    peticion = ""
    peticion += f'{mensaje.id}'
    peticion += f'{";"}'
    peticion += f'{mensaje.timestamp}'
    peticion += f'{";"}'
    for key, value in mensaje.header.items():
        peticion += f'{key + ":"}'
        peticion += f'{value + ","}'
    peticion += f'{";"}'
    for key, value in mensaje.body.items():
        peticion += f'{key + ":"}'
        peticion += f'{value + ","}'
    
    for i in range(1, 50):
        enviar_request(HOST, BROKERPORT, peticion)



    
if __name__ == "__main__":
    main()