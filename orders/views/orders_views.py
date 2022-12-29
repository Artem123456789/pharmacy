from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from libs.serialziers import NoneSerializer
from orders.handlers.orders_handlers import OrdersHandler
from orders.models import Order, OrderItem
from orders.serializers.orders_serializers import (
    OrderRetrieveSerializer,
    OrdersListSerializer,
    OrderCreateSerializer,
    OrderItemCreateSerializer,
    OrderItemUpdateSerializer
)


class OrdersViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = NoneSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        return {
            "create": OrderCreateSerializer,
            "list": OrdersListSerializer,
            "retrieve": OrderRetrieveSerializer
        }.get(self.action, NoneSerializer)


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = NoneSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action == "create":
            return self.queryset
        else:
            return OrderItem.objects.filter(order__user=self.request.user)

    def get_serializer_class(self):
        return {
            "create": OrderItemCreateSerializer,
            "update": OrderItemUpdateSerializer,
        }.get(self.action, NoneSerializer)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if OrdersHandler.add_order_item_count(serializer=serializer):
            return Response(status=status.HTTP_200_OK)

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        item: OrderItem = self.get_object()
        if item.order.is_in_work:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return super().destroy(request, *args, **kwargs)
