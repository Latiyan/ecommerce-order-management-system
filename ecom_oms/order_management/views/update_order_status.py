from rest_framework.views import APIView
from rest_framework.response import Response
from order_management.models import Order
from order_management.serializers.requests import UpdateOrderStatusRequest
from common.order_management_authenticate import order_management_authenticate
from django.utils.decorators import method_decorator


class UpdateOrderStatusView(APIView):
    """ Update order status """

    @method_decorator(order_management_authenticate)
    def dispatch(self, *args, **kwargs):
        """ Authenticate token and add appropriate attributes to request object """
        return super().dispatch(*args, **kwargs)

    def put(self, request, *args, **kwargs):

        # STEP 1: Pass the request data to serializer
        req_order = UpdateOrderStatusRequest(data=request.data)

        # STEP 2: Validate the request data
        validation_req_order = req_order.is_valid()
        if not validation_req_order:
            return Response({"status": 0,
                             "errors": req_order.errors,
                             "message": "Invalid data provided, Please have a look once."})

        try:
            # STEP 3: Get the validated data from serializer
            req_order_dict = req_order.validated_data

            order = Order.objects.get(id=req_order_dict["order_id"])

            order.order_status = req_order_dict["status"]
            order.save(update_fields=['order_status', 'updated_at'])

        except Exception as e:
            return Response({"status": 0,
                             "message": "Something went wrong, not able to update this order"})

        return Response({"status": 1,
                         "message": "Order Status Updated Successfully"})
