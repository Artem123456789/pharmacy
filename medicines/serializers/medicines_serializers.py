from rest_framework import serializers

from medicines.models import Medicine


class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = ["id", "name", "price", "manufacturer"]
