from django.contrib.admin import ModelAdmin, register
from .models.advertiser import Advertiser
from .models.ad import Ad
from .models.attributes import View, Click
from .services import ApproveStatusFilter


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

