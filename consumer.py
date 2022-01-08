import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
import django
django.setup()
import json
import pika
from products.models import Product
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmqhost'))
channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Admin Received {data}")
    if properties.content_type == 'product_created':
        product = Product.objects.get(pk=data)
        product.likes += 1
        product.save()
        print('Product liked')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
channel.close()
