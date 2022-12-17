from typing import List

from orders.models import Order
from django.contrib.auth import get_user_model


User = get_user_model()


class OrdersHandler:

    @staticmethod
    def user_orders(user: User) -> List[Order]:
        orders = Order.objects.filter(user=user)
        return orders
