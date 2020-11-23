from django.db import models
from advertiser_management.models.base_model import BaseAdvertising
from advertiser_management.models.advertiser import Advertiser


class Ad(BaseAdvertising):
    advertiser = models.ForeignKey(
        to=Advertiser,
        related_name='ads',
        verbose_name='تبلیغ کننده',
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=100,
        verbose_name='موضوع'
    )

    img_url = models.FileField(
        verbose_name='عکس تبلیغ',
    )

    link = models.URLField(
        verbose_name='ادرس سایت شما'
    )

    class Meta:
        verbose_name = 'تبلیغ'
        verbose_name_plural = 'تبلیغات'

    def __str__(self):
        return str(self.advertiser) + ' : ' + str(self.title)