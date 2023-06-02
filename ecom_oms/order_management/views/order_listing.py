from rest_framework.views import APIView
from rest_framework.response import Response
from order_management.models import Order, OrderItem


class OrderListingView(APIView):
    """ Order listing view """

    def get(self, request):
        order_list = Order.objects.all().order_by("created_at")

        data = []
        for order in order_list:
            details = {
                "order_id": order.id,
                "user_email": order.user.email,
                "order_status": order.order_status,
                "created_date": self.getTimeDateAsStr(order.created_at),
                "updated_date": self.getTimeDateAsStr(order.updated_at),
                "items": []
            }

            try:

                order_items = OrderItem.objects.filter(order=order.id)
            except OrderItem.DoesNotExist:
                continue

            for item in order_items:
                res = {
                    "name" : item.name,
                    "quantity" : item.quantity,
                    "price" : item.price,
                    "created_date": self.getTimeDateAsStr(item.created_at),
                    "updated_date": self.getTimeDateAsStr(item.updated_at)
                }

                details["items"].append(res)

            data.append(details)

        return Response({"status": 1,
                         "data": data})

    def getTimeDateAsStr(cls, time, format="%B %d, %Y"):
        """ Get time date as str """
        return time.strftime(format)
