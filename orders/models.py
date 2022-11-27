from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model

from libs.base_models import NamedModel
from medicines.models import Medicine


User = get_user_model()


class Order(NamedModel, TimeStampedModel):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)


class OrderItem(NamedModel, TimeStampedModel):
    medicine = models.ForeignKey(Medicine, blank=True, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.SET_NULL)
    count = models.IntegerField(blank=True, null=True)
