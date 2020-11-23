from django import forms


class CreateAdForm(forms.Form):
    advertiser_id = forms.IntegerField()

    title = forms.CharField(
        max_length=100
    )

    img_url = forms.URLField()

    link = forms.URLField()
