from django.forms import Form, IntegerField,CharField, URLField


class CreateAdForm(Form):
    advertiser_id = IntegerField()

    title = CharField(
        max_length=100
    )

    img_url = URLField()

    link = URLField()
