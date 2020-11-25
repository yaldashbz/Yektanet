from django.shortcuts import render, get_object_or_404
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from .models.advertiser import Advertiser
from .models.ad import Ad
from .models.attributes import Click, View
from .forms import CreateAdForm


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


def show_ads_all(request):
    advertisers = Advertiser.objects.all() #na intori
    # update_all_advertisers(advertisers)
    context = {'advertisers': advertisers}
    # ip = request.ip
    # View.objects.create(ad=ad, ip=ip)
    return render(request, 'advertiser_management/ads.html', context)


class AdOnClickRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'ad_on_click'

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['ad_id'])
        # ad.update_on_click()
        return ad.link
