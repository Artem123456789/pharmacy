from orders.models import OrderItem, Order
from django.contrib.auth import get_user_model

from orders.serializers.orders_serializers import OrderItemCreateSerializer

User = get_user_model()


class OrdersHandler:

    @staticmethod
    def add_order_item_count(serializer: OrderItemCreateSerializer) -> bool:
        existing_order_item = OrderItem.objects.filter(
            order=serializer.validated_data["order"],
            medicine=serializer.validated_data["medicine"]
        ).first()

        if existing_order_item:
            existing_order_item.count += serializer.validated_data["count"]
            existing_order_item.save()
            return True

        return False

    @staticmethod
    def set_order_into_work(order: Order) -> None:
        order.is_in_work = True
        order.save()
