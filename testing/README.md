Para ejecutar los servidores hay que ejecutar "py .\script.py" en la terminal.
Hice ese script tomando como referencia esta página: https://www.geeksforgeeks.org/run-one-python-script-from-another-in-python/

El programa levantará primero el broker, seguido del consumer y luego el producer, cada uno envía un mensaje para un mejor seguimiento, y tiene un formato del tipo: "(Nombre):      (Mensaje de aviso)"

- El producer mandará 50 veces el mismo mensaje.
- El broker tiene una cola de máximo 5 mensajes al mismo tiempo y le avisará al producer cuando un mensaje no se pudo meter a la cola.
- El consumer va a escribir lo que le dieron y va a esperar 5 segundos para hacer un intento de simulación de "Procesando"