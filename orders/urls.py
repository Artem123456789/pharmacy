from rest_framework.routers import DefaultRouter

from orders.views.orders_views import OrdersViewSet

app_name = "orders"

router = DefaultRouter()
router.register("orders", OrdersViewSet, basename="orders")

urlpatterns = router.get_urls()
