from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from orders.handlers.orders_handlers import OrdersHandler
from orders.models import Order
from orders.serializers.orders_serializers import OrdersModelSerializer


class OrdersViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin
):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OrdersModelSerializer

    # def list(self, request, *args, **kwargs):
    #     orders = OrdersHandler.user_orders(request.user)
    #     return Response(OrdersModelSerializer(orders, many=True).data)
