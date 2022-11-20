from django.contrib import admin

from medicines.models import Medicine


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ["name"]
