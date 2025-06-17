from rest_framework import generics
from .models import Order, OrderProduct
from .serializers import OrderSerializer, OrderProductSerializer
from .service_order import publish_order_created


class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        products = [{'product_id': p.product_id, 'quantity': p.quantity} for p in order.products.all()]
        publish_order_created(order.id, order.customer_id, products)


class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderProductListCreate(generics.ListCreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class OrderProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
