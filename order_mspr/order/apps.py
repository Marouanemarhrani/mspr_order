from django.apps import AppConfig

class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order'

    def ready(self):
        print("🚀 Order app ready → lancement RabbitMQ consumers")
        from .service_order import start_consumer_thread
        start_consumer_thread()
