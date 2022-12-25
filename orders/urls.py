from django.urls import path
from rest_framework import routers

from orders.views.orders_views import OrderListView, OrderDetailView

app_name = "orders"


urlpatterns = [
    path("orders/", OrderListView.as_view(), name="orders"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="orders")
]
