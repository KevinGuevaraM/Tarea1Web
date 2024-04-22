import subprocess
import time

if __name__ == "__main__":
    # Ejecute el broker
    broker_file = "message_broker.py"
    subprocess.Popen(["python", broker_file], shell=True)

    # Esperar para que no explote el asunto
    time.sleep(2)

    # Ejecute el productor
    producer_file = "producer.py"
    subprocess.Popen(["python", producer_file], shell=True)

    # Ejecute al consumidor
    consumer_file = "consumer.py"
    subprocess.Popen(["python", consumer_file], shell=True)

    print("Se iniciaron todos")