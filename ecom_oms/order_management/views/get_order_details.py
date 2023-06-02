from rest_framework.views import APIView
from rest_framework.response import Response
from order_management.models import Order


class GetOrderDetailsView(APIView):
    """ Order listing view """

    def get(self, request, order_id):
        try:

            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            raise Exception("Order does not exists")

        details = {
            "order_id": order.id,
            "user_email": order.user.email,
            "order_status": order.order_status,
            "created_date": self.getTimeDateAsStr(order.created_at),
            "updated_date": self.getTimeDateAsStr(order.updated_at),
        }

        return Response({"status": 1,
                         "details": details})

    def getTimeDateAsStr(cls, time, format="%B %d, %Y"):
        """ Get time date as str """
        return time.strftime(format)
