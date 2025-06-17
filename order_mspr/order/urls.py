from django.urls import path
from .views import (
    OrderListCreate,
    OrderRetrieveUpdateDestroy,
    OrderProductListCreate,  # ← Ceci doit correspondre au nom exact
    OrderProductRetrieveUpdateDestroy,
)

urlpatterns = [
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroy.as_view(), name='order-detail'),
    path('order-products/', OrderProductListCreate.as_view(), name='orderproduct-list-create'),
    path('order-products/<int:pk>/', OrderProductRetrieveUpdateDestroy.as_view(), name='orderproduct-detail'),
]
