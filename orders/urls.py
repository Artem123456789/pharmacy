from rest_framework import routers

from orders.views.orders_views import OrdersViewSet

app_name = "orders"

router = routers.DefaultRouter()
router.register(b"orders", OrdersViewSet, basename="orders")

urlpatterns = router.get_urls()
