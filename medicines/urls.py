from django.urls import path

from medicines.views.medicines_views import MedicinesList

urlpatterns = [
    path("/medicines", MedicinesList.as_view())
]
