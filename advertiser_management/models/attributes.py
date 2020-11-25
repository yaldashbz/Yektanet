from django.db.models import Model, DateTimeField, GenericIPAddressField, ForeignKey, CASCADE
from django.utils import timezone

from .ad import Ad


class BaseAttribute(Model):
    ip = GenericIPAddressField()

    time = DateTimeField(
        default=timezone.now
    )

    class Meta:
        abstract = True


class Click(BaseAttribute):
    ad = ForeignKey(
        to=Ad,
        related_name='clicks',
        on_delete=CASCADE
    )

    def __str__(self):
        return str(self.ad.id) + ' : ' + self.ip + ' - ' + str(self.time)


class View(BaseAttribute):
    ad = ForeignKey(
        to=Ad,
        related_name='views',
        on_delete=CASCADE
    )

    def __str__(self):
        return str(self.ad.id) + ' : ' + self.ip + ' - ' + str(self.time)
