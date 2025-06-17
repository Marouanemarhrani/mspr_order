from django.db import models

class Order(models.Model):
    customer_id = models.IntegerField()
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} - Customer {self.customer_id}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="products")
    product_id = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        unique_together = (('order', 'product_id'),)
