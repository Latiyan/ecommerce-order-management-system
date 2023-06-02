"""
This module consists of order status related choices
"""
from django.db import models


class OrderStatus(models.TextChoices):
    """ Integer order status """
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
    PROCESSING = "PROCESSING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    REFUNDED = "REFUNDED"
    FAILED = "FAILED"
