from django.contrib import admin

from orders.models import OrderItem, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ["user"]

    list_display = ["user", "issue_date", "is_ready", "is_issued"]
    list_filter = ["is_ready", "is_issued"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ["medicine"]

    list_display = ["medicine", "count"]

