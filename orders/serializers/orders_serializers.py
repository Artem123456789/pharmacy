from rest_framework import serializers

from medicines.models import Medicine, Manufacturer
from orders.models import Order, OrderItem


class ManufacturerOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = [
            "name"
        ]


class MedicineOrderSerializer(serializers.ModelSerializer):
    manufacturer = serializers.SerializerMethodField()

    def get_manufacturer(self, medicine: Medicine):
        return ManufacturerOrderSerializer(medicine.manufacturer).data

    class Meta:
        model = Medicine
        fields = [
            "name",
            "price",
            "manufacturer"
        ]


class OrderItemModelSerializer(serializers.ModelSerializer):
    medicine = serializers.SerializerMethodField()

    def get_medicine(self, order_item: OrderItem):
        return MedicineOrderSerializer(order_item.medicine).data

    class Meta:
        model = OrderItem
        fields = [
            "medicine",
            "count"
        ]


class OrdersModelSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    def get_items(self, order: Order):
        items = OrderItem.objects.filter(order=order)
        return OrderItemModelSerializer(items, many=True).data

    class Meta:
        model = Order
        fields = [
            "id",
            "issue_date",
            "is_ready",
            "is_issued",
            "items"
        ]
