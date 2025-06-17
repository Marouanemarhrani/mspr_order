FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r order_mspr/requirements.txt

ENV PYTHONPATH=/app/order_mspr

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "service_order.wsgi:application"]
