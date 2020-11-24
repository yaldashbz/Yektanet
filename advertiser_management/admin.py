from django.contrib.admin import ModelAdmin, register
from advertiser_management.models.advertiser import Advertiser
from advertiser_management.models.ad import Ad


@register(Advertiser)
class AdvertiserAdmin(ModelAdmin):
    fields = ['name']


@register(Ad)
class AdAdmin(ModelAdmin):
    exclude = ['clicks', 'views']
