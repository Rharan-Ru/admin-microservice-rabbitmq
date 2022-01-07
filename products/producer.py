import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmqhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='hello', body=json.dumps(body), properties=properties)
    print(f"Send {body}")
