from rest_framework.views import APIView
from rest_framework.response import Response
from order_management.models import Order, OrderItem
from order_management.serializers.requests import CreateOrderRequest


class CreateOrderView(APIView):
    """ Create Order View """

    def post(self, request, *args, **kwargs):

        # STEP 1: Pass the request data to serializer
        req_order = CreateOrderRequest(data=request.data)

        # STEP 2: Validate the request data
        validation_req_order = req_order.is_valid()
        if not validation_req_order:
            raise Exception("Invalid data provided, Please have a look once.", errors=req_order.errors)

        OrderId = 0
        try:
            # STEP 3: Get the validated data from serializer
            req_order_dict = req_order.validated_data

            with transaction.atomic():
                OrderId = self.create_order(req_order_dict)

        except Exception as e:
            raise Exception("Something went wrong, not able to create this order")

        return Response({"status": 1,
                         "Order_id": OrderId,
                         "message": "Order Created Successfully"})

    def create_order(self, data):
        return 1
