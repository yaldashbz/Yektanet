from django.contrib.admin import ModelAdmin, register
from advertiser_management.models.advertiser import Advertiser
from advertiser_management.models.ad import Ad
from advertiser_management.models.attributes import View, Click
from advertiser_management.services import ApproveStatusFilter


@register(Ad)
class AdAdmin(ModelAdmin):
    fields = ['approve']
    search_fields = ['title']
    list_filter = [ApproveStatusFilter]


@register(Advertiser)
class AdvertiserAdmin(ModelAdmin):
    fields = ['name']


# debug
@register(Click)
class ClickAdmin(ModelAdmin):
    pass


@register(View)
class ViewAdmin(ModelAdmin):
    pass

