from django.contrib import admin
from advertiser_management.models.advertiser import Advertiser
from advertiser_management.models.ad import Ad


@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    exclude = ['clicks', 'views']
