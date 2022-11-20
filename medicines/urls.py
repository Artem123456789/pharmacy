from django.urls import path, include
from rest_framework.routers import DefaultRouter

from medicines.views.medicines_views import MedicinesViewSet

app_name = "medicines"

router = DefaultRouter()
router.register(r"medicines", MedicinesViewSet, basename="medicines")

urlpatterns = [
    path("", include(router.urls))
]
