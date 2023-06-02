from django.urls import path
from order_management.views import *

urlpatterns = [
    path('create_order/', CreateOrderView.as_view()),
    path('order_listing/', OrderListingView.as_view()),
    path('get_order_details/<int:order_id>', GetOrderDetailsView.as_view()),
]
