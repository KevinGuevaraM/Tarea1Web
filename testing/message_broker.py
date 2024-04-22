from queue import Queue
import socket
import string

HOST = "127.0.0.1" # Esto es local :B
PORT = 1789 #Puerto al que escucha
PRODUCERPORT = 1799 # Puerto del Producer
CONSUMERPORT = 1800 # Puerto del consumidor

##< 
class Broker:
    """!
    @brief Clase que representa un broker con colas

    """
    def __init__(self):
        """!
        @brief Constructor de la clase Broker

        Inicializa los atributos de la clase.

        """
        # Sí, sigo sin entender por qué el nombre
        self.queue_name: str = ""
        self.queue: Queue = None
    
    def create_queue(self, queue_name: str, max_size: int=1000):
        """!
        @brief Crea una cola para el broker

        Parametros : 
            @param queue_name : str => Nombre del queue (No sé por qué existe)
            @param max_size : int = 1000 => Maximo tamaño de la cola del broker (1000 por defecto)

        """
        self.queue_name = queue_name
        self.queue = Queue(max_size)

    def flush_queue(self, n: int = None):
        """!
        @brief elimina n elementos de la cola (Si no le da parámetros va a borrar toda la cola)

        Parametros : 
            @param n : int = None => cantidad de elementos de la cola a eliminar

        """
        if n == None:
            while not self.queue.empty():
                self.queue.get()
        else:
            for i in range(n):
                self.queue.get()
    
    def delete_queue(self, queue_name: str):
        """!
        @brief Elimina la cola actual

        Parametros : 
            @param queue_name : str => Hola.

        """
        del self.queue
        self.queue = None

    def enqueue(self, queue_name, msg):
        """!
        @brief Introduce a la cola un mensaje

        Parametros : 
            @param queue_name => Un nombre
            @param msg => Dato a meter en la cola

        """
        if self.queue.full():
            return False
        else:
            self.queue.put(msg)
            return True

    def dequeue(self, host, port):
        """!
        @brief Saca de la cola un elemento y le hace push a un consumidor

        Parametros : 
            @param host => host del consumidor
            @param port => puerto en el que está escuchando el consumidor

        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            try:
                s.connect((host, port))
                s.recv(1)
                peticion = f'{self.queue.get()}'
                s.sendall(peticion.encode())
                print("BROKER:       Se logró enviar el elemento al consumidor, quedan: " + str(self.queue.qsize()))
            except TimeoutError:
                print("BROKER:       El consumidor está ocupado, quedan "+ str(self.queue.qsize()))


def main():
    broker = Broker()
    broker.create_queue("Ola", 5)
    tiempoReintento = 5
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.settimeout(tiempoReintento)
        while True:
                try:
                    s.listen()
                    connection, addr = s.accept()
                    data = connection.recv(1024)
                    data = (data.decode())
                    with connection:
                        if broker.enqueue("Un Nombre", data) == True:
                            peticion = f'{1}'
                            connection.sendall(peticion.encode())
                        else:
                            connection.sendall((f'{0}').encode())
                            
                        broker.dequeue(HOST, CONSUMERPORT)

                except TimeoutError:
                    if broker.queue.empty() == False:
                        print("BROKER:       A la cola le quedan elementos, intentaré darle elemento al consumidor")
                        broker.dequeue(HOST, CONSUMERPORT)

if __name__ == "__main__":
    main()