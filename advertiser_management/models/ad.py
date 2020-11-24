from django.db.models import ForeignKey, CharField, URLField, CASCADE
from advertiser_management.models.base_model import BaseAdvertising
from advertiser_management.models.advertiser import Advertiser


class Ad(BaseAdvertising):
    advertiser = ForeignKey(
        to=Advertiser,
        related_name='ads',
        verbose_name='تبلیغ کننده',
        on_delete=CASCADE
    )

    title = CharField(
        max_length=100,
        verbose_name='موضوع'
    )

    img_url = URLField(
        verbose_name=' ادرس عکس تبلیغ'
    )

    link = URLField(
        verbose_name='ادرس سایت شما'
    )

    class Meta:
        verbose_name = 'تبلیغ'
        verbose_name_plural = 'تبلیغات'

    def __str__(self):
        return str(self.advertiser) + ' : ' + str(self.title)

    def update_on_click(self):
        self.clicks += 1
        self.advertiser.clicks += 1
        self.save(update_fields=['clicks'])
        self.advertiser.save(update_fields=['clicks'])

    def update_on_view(self):
        self.views += 1
        self.advertiser.views += 1
        self.save(update_fields=['views'])
        self.advertiser.save(update_fields=['views'])
