from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from advertiser_management.models.advertiser import Advertiser
from advertiser_management.models.ad import Ad
from advertiser_management.models.attributes import Click, View
from advertiser_management.forms import CreateAdForm


class CreateAdFormView(FormView):
    template_name = 'advertiser_management/create_ad.html'
    form_class = CreateAdForm
    success_url = '/advertiser-management/all-ads'

    def form_valid(self, form):
        advertiser_id = form.cleaned_data['advertiser_id']
        try:
            advertiser = Advertiser.objects.get(pk=advertiser_id)
            img_url = form.cleaned_data['img_url']
            link = form.cleaned_data['link']
            title = form.cleaned_data['title']
            Ad.objects.create(advertiser=advertiser, title=title, img_url=img_url, link=link)

            return super().form_valid(form)

        except(KeyError, Advertiser.DoesNotExist):
            return render(self.request, 'advertiser_management/create_ad.html', {
                'form': form,
                'error_message': 'Advertiser ID is not valid.'
            })


class ShowAllAdsListView(ListView):
    template_name = 'advertiser_management/ads.html'
    model = Advertiser

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        advertisers = Advertiser.objects.all()
        update_advertisers_view(advertisers, self.request.ip)
        context['advertisers'] = advertisers
        return context


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


def update_advertisers_view(advertisers, ip):
    for advertiser in advertisers:
        update_ads(advertiser, ip)


def update_ads(advertiser, ip):
    for ad in advertiser.ads.all():
        View.objects.create(ad=ad, ip=ip)
