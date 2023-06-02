"""
This module consists of order status related choices
"""
from django.db import models


class OrderStatus(models.IntegerChoices):
    """ Integer order status """
    PENDING = 1
    CANCELLED = 2
    PROCESSING = 3
    SHIPPED = 4
    DELIVERED = 5
    REFUNDED = 6
    FAILED = 7


class OrderTextStatus(models.TextChoices):
    """ Text choicdes for order status """
    PENDING = "Pending"
    CANCELLED = "Cancelled"
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    REFUNDED = "Refunded"
    FAILED = "Failed"
