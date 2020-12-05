from django.db.models import Model, ForeignKey, CharField, URLField, CASCADE, Count, F
from django.db.models.functions import Cast
from django.db.models import Count, Q, F, FloatField
from django.utils import timezone

from advertiser_management.models.advertiser import Advertiser


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

    @staticmethod
    def get_total_ctr(start_time, end_time):
        return Ad.objects.annotate(
            total_views=Count(
                F('views'),
                distinct=True,
                filter=Q(
                    views__time__range=(start_time, end_time)
                )
            )
        ).filter(
            total_views__gt=0
        ).annotate(
            ctr=Cast(Count(
                F('clicks'),
                distinct=True,
                filter=Q(
                    clicks__time__range=(start_time, end_time)
                )
            ), FloatField()) / Cast(Count(
                F('views'),
                distinct=True,
                filter=Q(
                    views__time__range=(start_time, end_time)
                ),
                output_field=FloatField()
            ), FloatField())
        ).order_by('-ctr')

    @staticmethod
    def get_total_clicks_views(start_time, end_time, delta):
        ads = Ad.objects.all()
        response = dict()
        for ad in ads:
            ad_response = list()
            start = start_time
            while start < end_time:
                end = start + timezone.timedelta(hours=delta)
                d = ad.get_dict_in_time_range(start_time=start, end_time=end)
                ad_response.append(d)

                start = end

            response.update({ad: ad_response})

        return response

    def get_dict_in_time_range(self, start_time, end_time):
        clicks_count = self.clicks.filter(
            time__range=(start_time, end_time)
        ).count()

        views_count = self.views.filter(
            time__range=(start_time, end_time)
        ).count()

        d = dict()
        d.update({
            'start_time': start_time,
            'end_time': end_time,
            'total_clicks': clicks_count,
            'total_view': views_count,
        })
        return d

    def get_closest_view(self, ip, time):
        return self.views.filter(
            ip=ip,
            time__lt=time
        ).order_by('-time')[0]
