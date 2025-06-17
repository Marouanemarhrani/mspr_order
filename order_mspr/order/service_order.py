import json
import pika
import threading
import time


def publish_order_created(order_id, customer_id, products):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        channel.exchange_declare(exchange='service_exchange', exchange_type='topic', durable=True)

        message = {
            'order_id': order_id,
            'customer_id': customer_id,
            'products': products
        }

        channel.basic_publish(
            exchange='service_exchange',
            routing_key='order.created',
            body=json.dumps(message)
        )
        print(f"📤 Published order.created: {message}")
        connection.close()
    except Exception as e:
        print(f"❌ Failed to publish order.created: {e}")


def callback_products(ch, method, properties, body):
    print("📥 Message reçu depuis product_exchange :", body)


def consume_products():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
            channel = connection.channel()
            channel.exchange_declare(exchange='product_exchange', exchange_type='topic', durable=True)
            channel.queue_declare(queue='order_service_product_queue', durable=True)
            channel.queue_bind(exchange='product_exchange', queue='order_service_product_queue', routing_key='product.list')

            channel.basic_consume(queue='order_service_product_queue', on_message_callback=callback_products, auto_ack=True)
            print("👂 Order écoute les messages 'product.list'...")
            channel.start_consuming()
        except Exception as e:
            print(f"❌ Erreur RabbitMQ (consume_products) : {e}")
            time.sleep(5)


def start_consumer_thread():
    thread = threading.Thread(target=consume_products, daemon=True)
    thread.start()
