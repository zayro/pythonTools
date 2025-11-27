import pika

# 1. Establecer la conexión
# Reemplaza 'localhost' por la dirección de tu broker si no está en el mismo equipo.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 2. Declarar la cola
# Esto crea la cola si aún no existe.
channel.queue_declare(queue='hola_cola')

# 3. Publicar el mensaje
channel.basic_publish(exchange='',
                      routing_key='hola_cola',
                      body='¡Hola, mundo!')

print(" [x] Enviado '¡Hola, mundo!'")

# 4. Cerrar la conexión
connection.close()
