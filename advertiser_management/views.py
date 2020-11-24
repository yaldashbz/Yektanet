from django.shortcuts import render, get_object_or_404
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect

from advertiser_management.models.advertiser import Advertiser
from advertiser_management.models.ad import Ad
from advertiser_management.forms import CreateAdForm

from advertiser_management.services import update_all_advertisers


def create_ad(request):
    form = CreateAdForm(request.POST)
    if form.is_valid():
        advertiser_id = request.POST['advertiser_id']
        try:
            advertiser = Advertiser.objects.get(pk=advertiser_id)
            img_url = form.cleaned_data['img_url']
            link = request.POST['link']
            title = request.POST['title']
            Ad.objects.create(advertiser=advertiser, title=title, img_url=img_url, link=link)
            return HttpResponseRedirect('/advertiser-management/all-ads')

        except(KeyError, Advertiser.DoesNotExist):
            return render(request, 'advertiser_management/create_ad.html', {
                'form': form,
                'error_message': 'Advertiser ID is not valid.'
            })

    return render(request, 'advertiser_management/create_ad.html', {
        'form': form
    })


def show_ads_all(request):
    advertisers = Advertiser.objects.all()
    update_all_advertisers(advertisers)
    context = {'advertisers': advertisers}
    return render(request, 'advertiser_management/ads.html', context)


class AdOnClickRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'ad_on_click'

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['ad_id'])
        ad.update_on_click()
        return ad.link
