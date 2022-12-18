from django.urls import path
from rest_framework import routers

from orders.views.orders_views import OrderListView

app_name = "orders"


urlpatterns = [
    path("orders/", OrderListView.as_view(), name="orders"),
]
