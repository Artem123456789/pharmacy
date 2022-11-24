from django.contrib import admin

from medicines.models import Medicine, Manufacturer


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "manufacturer"]
    search_fields = ["name"]

    list_filter = ["manufacturer"]


@admin.register(Manufacturer)
class Manufacturer(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
