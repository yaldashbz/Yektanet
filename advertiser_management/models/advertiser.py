from django.db.models import Model, CharField


class Advertiser(Model):
    name = CharField(
        max_length=20,
        verbose_name='نام'
    )

    class Meta:
        verbose_name = 'تبلیغ کننده'
        verbose_name_plural = 'تبلیغ کنندگان'

    def __str__(self):
        return self.name
