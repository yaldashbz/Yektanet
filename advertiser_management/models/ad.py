from django.db.models import Model, ForeignKey, CharField, URLField, CASCADE
from .advertiser import Advertiser


class Ad(Model):
    APPROVAL_CHOICES = (
        ('accepted', 'قبول'),
        ('denied', 'رد'),
    )

    advertiser = ForeignKey(
        to=Advertiser,
        related_name='ads',
        verbose_name='تبلیغ کننده',
        on_delete=CASCADE
    )

    approve = CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        verbose_name='وضعیت',
        default='denied'
    )

    title = CharField(
        max_length=100,
        verbose_name='موضوع'
    )

    img_url = URLField(
        verbose_name=' ادرس عکس تبلیغ',
    )

    link = URLField(
        verbose_name='ادرس سایت شما'
    )

    class Meta:
        verbose_name = 'تبلیغ'
        verbose_name_plural = 'تبلیغات'

    def __str__(self):
        return str(self.advertiser) + ' : ' + str(self.title)
