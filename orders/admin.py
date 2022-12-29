from django.contrib import admin

from orders.models import OrderItem, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ["user"]

    list_display = ["user", "delivery_date", "is_ready", "is_issued", "is_in_work"]
    list_filter = ["is_ready", "is_issued", "is_in_work"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ["medicine"]

    list_display = ["medicine", "count"]

