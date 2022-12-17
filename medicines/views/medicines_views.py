from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from medicines.paginators import MedicinesListPaginator
from medicines.serializers import medicines_serializers
from medicines.models import Medicine


class MedicinesList(generics.ListAPIView):
    serializer_class = medicines_serializers.MedicineSerializer
    queryset = Medicine.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MedicinesListPaginator
