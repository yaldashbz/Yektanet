from django.contrib import admin
from .models.ad import Ad
from .models.advertiser import Advertiser


@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    exclude = ['clicks', 'views']
