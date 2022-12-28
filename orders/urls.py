from rest_framework.routers import DefaultRouter

from orders.views.orders_views import OrdersViewSet, OrderItemViewSet

app_name = "orders"

router = DefaultRouter()
router.register("orders", OrdersViewSet, basename="orders")
router.register("order-items", OrderItemViewSet, basename="order-items")

urlpatterns = router.get_urls()
