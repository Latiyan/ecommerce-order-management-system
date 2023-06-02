from django.db import models
from django.contrib.auth.models import User
from common.order_status import OrderStatus


# Create your models here.

class Order(models.Model):
    """ Order model """
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    order_status = models.TextField(db_index=True, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Dunder method to return human redable names """
        return f"OrderID({self.id})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        """ Dunder method to return human redable names """
        return f"OrderID({self.order.id}) - Name({self.name}) - Qty({self.quantity})"
