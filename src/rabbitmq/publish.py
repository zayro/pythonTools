import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar exchange (direct) y cola opcionalmente
exchange_name = 'mi_exchange'
routing_key = 'mi_routing'
channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)

message = '¡Hola, mundo con exchange y routing key!'
# Mensaje persistente (delivery_mode=2)
channel.basic_publish(
    exchange=exchange_name,
    routing_key=routing_key,
    body=message,
    properties=pika.BasicProperties(delivery_mode=2)
)

print(f" [x] Enviado a exchange='{exchange_name}' routing_key='{routing_key}': {message}")

connection.close()
# ...existing code...