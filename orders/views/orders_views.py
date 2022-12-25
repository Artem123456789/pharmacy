from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from libs.permissions import IsOwnerPermission
from orders.handlers.orders_handlers import OrdersHandler
from orders.models import Order
from orders.serializers.orders_serializers import OrdersModelSerializer, OrdersListSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrdersListSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user_orders = OrdersHandler.user_orders(request.user)
        return Response(OrdersListSerializer(user_orders, many=True).data)


class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrdersModelSerializer
    permission_classes = [IsOwnerPermission]
