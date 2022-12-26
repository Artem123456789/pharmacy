from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from libs.serialziers import NoneSerializer
from orders.models import Order
from orders.serializers.orders_serializers import OrderRetrieveSerializer, OrdersListSerializer


class OrdersViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        return {
            "list": OrdersListSerializer,
            "retrieve": OrderRetrieveSerializer
        }.get(self.action, NoneSerializer)
