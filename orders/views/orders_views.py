from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from orders.handlers.orders_handlers import OrdersHandler
from orders.models import Order, OrderItem
from orders.serializers.orders_serializers import OrdersModelSerializer, OrderItemModelSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrdersModelSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user_orders = OrdersHandler.user_orders(request.user)
        return Response(OrdersModelSerializer(user_orders, many=True).data)
