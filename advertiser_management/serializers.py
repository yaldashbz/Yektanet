from rest_framework.serializers import ModelSerializer, FloatField

from advertiser_management.models import Advertiser, Ad, Click


class AdCTRSerializer(ModelSerializer):
    ctr = FloatField(read_only=True)

    class Meta:
        model = Ad
        fields = ['title', 'ctr']


class ClickSerializer(ModelSerializer):
    class Meta:
        model = Click
        fields = ['duration']


class AdEstimationSerializer(ModelSerializer):
    clicks = ClickSerializer(many=True)

    class Meta:
        model = Ad
        fields = ['title', 'clicks']


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = ['title', 'img_url', 'link', 'advertiser']


class AdvertiserSerializer(ModelSerializer):
    ads = AdSerializer(many=True, read_only=True)

    class Meta:
        model = Advertiser
        fields = ['name', 'ads']
