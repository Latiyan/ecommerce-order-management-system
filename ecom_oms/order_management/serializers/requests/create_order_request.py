from rest_framework import serializers


class ItemsRequest(serializers.Serializer):
    """ Serializer to validate Order Items """
    name = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(min_value=0)


class CreateOrderRequest(serializers.Serializer):
    """ Request serializer for Create Order Request """
    user = serializers.IntegerField(min_value=1)
    status = serializers.CharField(max_length=150)
    cart = ItemsRequest(many=True)
