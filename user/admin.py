from django.contrib.admin import ModelAdmin, register

from user.models import Customer


@register(Customer)
class CustomerAdmin(ModelAdmin):
    pass


