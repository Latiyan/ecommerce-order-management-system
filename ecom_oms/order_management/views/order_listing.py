from rest_framework.views import APIView
from rest_framework.response import Response
from order_management.models import Order


class OrderListingView(APIView):
    """ Order listing view """

    def get(self, request):
        order_list = Order.objects.all()

        res = []
        for order in order_list:
            details = {
                "order_id": order.id,
                "user_email": order.user.email,
                "order_status": order.order_status,
                "created_date": self.getTimeDateAsStr(order.created_at),
                "updated_date": self.getTimeDateAsStr(order.updated_at),
            }

            res.append(details)

        return Response({"status": 1,
                         "data": res})

    def getTimeDateAsStr(cls, time, format="%B %d, %Y"):
        """ Get time date as str """
        return time.strftime(format)
