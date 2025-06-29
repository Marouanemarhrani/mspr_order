#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# In manage.py
from django.core.management import execute_from_command_line
from order.service_order import start_consumer_thread  # Import the consumer
    # Start the RabbitMQ consumer in a background thread
   

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service_order.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
    start_consumer_thread()
    execute_from_command_line(sys.argv)
