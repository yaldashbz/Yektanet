from django.db import models
from advertiser_management.models.base_model import BaseAdvertising


class Advertiser(BaseAdvertising):
    name = models.CharField(
        max_length=20,
        verbose_name='نام'
    )

    class Meta:
        verbose_name = 'تبلیغ کننده'
        verbose_name_plural = 'تبلیغ کنندگان'

    def __str__(self):
        return self.name

