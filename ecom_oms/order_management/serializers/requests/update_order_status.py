from rest_framework import serializers
from common.order_status import OrderStatus


class UpdateOrderStatusRequest(serializers.Serializer):
    order_id = serializers.IntegerField(min_value=1)
    status = serializers.ChoiceField(choices=OrderStatus.choices)
