from django.urls import path

from medicines.views.medicines_views import MedicinesList

app_name = "medicines"

urlpatterns = [
    path("medicines/", MedicinesList.as_view())
]
