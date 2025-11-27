import pika

def callback(ch, method, properties, body):
    print(f" [x] Recibido: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Asegura que la cola existe
channel.queue_declare(queue='hola_cola')

# Evita procesar múltiples mensajes simultáneamente
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='hola_cola', on_message_callback=callback)

print(" [*] Esperando mensajes. Para salir: Ctrl+C")
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    connection.close()
    print("Conexión cerrada")