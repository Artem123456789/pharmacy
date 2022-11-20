from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext as _

from libs.base_models import NamedModel


class Medicine(NamedModel, TimeStampedModel):
    price = models.FloatField(blank=True, verbose_name=("Цена"), null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Препарат")
        verbose_name_plural = _("Препараты")
        ordering = ["-created"]

