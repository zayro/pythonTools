# ...existing code...
import pika

def callback(ch, method, properties, body):
    print(f" [x] Recibido (exchange={method.exchange} routing_key={method.routing_key}): {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

exchange_name = 'mi_exchange'
routing_key = 'mi_routing'
queue_name = 'cola_procesadora'  # o '' para cola efímera con name generado por el broker

# Declarar exchange y cola, y enlazar con routing_key
channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)
channel.queue_declare(queue=queue_name, durable=True)
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name, on_message_callback=callback)

print(f" [*] Esperando mensajes en queue='{queue_name}' bound a exchange='{exchange_name}' routing_key='{routing_key}'")
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    connection.close()
    print("Conexión cerrada")
# ...existing code...