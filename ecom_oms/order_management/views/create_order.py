from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
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
            return Response({"status": 0,
                             "errors": req_order.errors,
                             "message": "Invalid data provided, Please have a look once."})

        try:
            # STEP 3: Get the validated data from serializer
            req_order_dict = req_order.validated_data

            order = self.create_order(req_order_dict)

        except Exception as e:
            return Response({"status": 0,
                             "message": "Something went wrong, not able to create this order"})

        return Response({"status": 1,
                         "Order_id": order.id,
                         "message": "Order Created Successfully"})

    def create_order(self, data):
        # First get user object from user id
        try:
            user = User.objects.get(id=data["user"])
        except User.DoesNotExist:
            raise Exception("User does not exists, please verify the user id once.")

        # Now create an order with the user and status provided
        order = Order(user=user, order_status=data["status"])
        order.save()

        # For each item in the request create an order item and associate it with the order
        for item in data["items"]:

            order_item = OrderItem(order=order, name=item["name"], quantity=item["quantity"], price=item["price"])
            order_item.save()

        return order
