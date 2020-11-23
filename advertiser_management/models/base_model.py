from django.db import models


class BaseAdvertising(models.Model):
    clicks = models.PositiveBigIntegerField(
        default=0
    )

    views = models.PositiveBigIntegerField(
        default=0
    )

    class Meta:
        abstract = True
