from rest_framework.views import APIView
from rest_framework.response import Response
from order_management.models import Order, OrderItem


class GetOrderDetailsView(APIView):
    """ Order listing view """

    def get(self, request, order_id):
        try:

            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({"status": 0,
                             "message": "Order does not exist, please check the order ID."})

        try:

            order_items = OrderItem.objects.filter(order=order_id)
        except OrderItem.DoesNotExist:
            return Response({"status": 0,
                             "message": "Order does not have any associated items."})

        details = {
            "order_id": order.id,
            "user_email": order.user.email,
            "order_status": order.order_status,
            "created_date": self.getTimeDateAsStr(order.created_at),
            "updated_date": self.getTimeDateAsStr(order.updated_at),
            "items": []
        }

        for item in order_items:
            res = {
                "name" : item.name,
                "quantity" : item.quantity,
                "price" : item.price,
                "created_date": self.getTimeDateAsStr(item.created_at),
                "updated_date": self.getTimeDateAsStr(item.updated_at)
            }

            details["items"].append(res)


        return Response({"status": 1,
                         "details": details})

    def getTimeDateAsStr(cls, time, format="%B %d, %Y"):
        """ Get time date as str """
        return time.strftime(format)
