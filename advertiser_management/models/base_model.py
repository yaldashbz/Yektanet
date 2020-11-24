from django.db.models import Model, PositiveBigIntegerField


class BaseAdvertising(Model):
    clicks = PositiveBigIntegerField(
        default=0
    )

    views = PositiveBigIntegerField(
        default=0
    )

    class Meta:
        abstract = True
