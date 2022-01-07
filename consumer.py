import json
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmqhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Main Received {data}")


channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
channel.close()
