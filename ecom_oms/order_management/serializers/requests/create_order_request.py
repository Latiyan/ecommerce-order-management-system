from rest_framework import serializers
from common.order_status import OrderStatus


class ItemsRequest(serializers.Serializer):
    """ Serializer to validate Order Items """
    name = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(min_value=0)


class CreateOrderRequest(serializers.Serializer):
    """ Request serializer for Create Order Request """
    user = serializers.IntegerField(min_value=1)
    status = serializers.ChoiceField(choices=OrderStatus.choices)
    cart = ItemsRequest(many=True)
