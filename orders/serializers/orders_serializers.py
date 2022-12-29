from rest_framework import serializers

from medicines.models import Medicine, Manufacturer
from orders.constants import SHORT_LABEL_MAX_ITEMS
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
            "uuid",
            "medicine",
            "count"
        ]


class OrdersListSerializer(serializers.ModelSerializer):
    short_label = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()

    def get_short_label(self, order: Order):
        items = OrderItem.objects.filter(order=order)[:SHORT_LABEL_MAX_ITEMS]
        label = ""
        for item in items:
            label += item.medicine.name + ", "

        return "No items" if label == "" else label.rstrip(", ") + "..."

    def get_total_amount(self, order: Order):
        amount = 0
        items = OrderItem.objects.filter(order=order)
        for item in items:
            amount += item.medicine.price * item.count

        return amount

    class Meta:
        model = Order
        fields = [
            "uuid",
            "delivery_date",
            "is_in_work",
            "is_ready",
            "is_issued",
            "short_label",
            "total_amount"
        ]


class OrderRetrieveSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()

    def get_items(self, order: Order):
        items = OrderItem.objects.filter(order=order)
        return OrderItemModelSerializer(items, many=True).data

    def get_total_amount(self, order: Order):
        amount = 0
        items = OrderItem.objects.filter(order=order)
        for item in items:
            amount += item.medicine.price * item.count

        return amount

    class Meta:
        model = Order
        fields = [
            "uuid",
            "delivery_date",
            "is_in_work",
            "is_ready",
            "is_issued",
            "items",
            "total_amount"
        ]


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            "uuid",
            "user"
        ]


class OrderItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = [
            "uuid",
            "medicine",
            "order",
            "count"
        ]


class OrderItemUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = [
            "count"
        ]
