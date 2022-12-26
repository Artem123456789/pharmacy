from datetime import datetime, timedelta

from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from medicines.models import Medicine
from orders.constants import DEFAULT_DELIVERY_DATE_SHIFT

User = get_user_model()


class Order(TimeStampedModel):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    delivery_date = models.DateField(default=datetime.now().date() + timedelta(days=DEFAULT_DELIVERY_DATE_SHIFT))
    is_ready = models.BooleanField(default=False)
    is_issued = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")


class OrderItem(TimeStampedModel):
    medicine = models.ForeignKey(Medicine, blank=True, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.SET_NULL)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _("Товар заказа")
        verbose_name_plural = _("Товары заказа")
