from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from medicines.serializers import medicines_serializers
from medicines.models import Medicine


class MedicinesViewSet(viewsets.ModelViewSet):
    serializer_class = medicines_serializers.MedicineSerializer
    queryset = Medicine.objects.all()
    permission_classes = [IsAuthenticated]
