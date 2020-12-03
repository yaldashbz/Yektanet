from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic.base import RedirectView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertiser_management.models.advertiser import Advertiser
from advertiser_management.models.ad import Ad
from advertiser_management.models.attributes import Click, View
from advertiser_management.serializers import AdvertiserSerializer, AdSerializer


class AdOnClickRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'ad_on_click'

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['ad_id'])
        ip = self.request.ip
        now = timezone.now()
        view = get_closest_view(ad, ip, now)
        Click.objects.create(ad=ad, ip=ip, duration=now - view.time)
        return ad.link


def get_closest_view(ad, ip, time):
    return ad.views.filter(
        ip=ip,
        time__lt=time
    ).order_by('-time')[0]


class AdViewSet(ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Advertiser.objects.all()
        update_advertisers_view(queryset, self.request.ip)
        serializer = AdvertiserSerializer(queryset, many=True)
        return Response(
            serializer.data
        )


def update_advertisers_view(advertisers, ip):
    for advertiser in advertisers:
        update_ads(advertiser, ip)


def update_ads(advertiser, ip):
    for ad in advertiser.ads.all():
        View.objects.create(ad=ad, ip=ip)
