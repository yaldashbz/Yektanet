from django.shortcuts import render
from django.views.generic import ListView, FormView

from advertiser_management.forms import CreateAdForm
from advertiser_management.models import Ad, Advertiser
from advertiser_management.views.user_views import update_advertisers_view


class EstimateDurationListView(ListView):
    template_name = 'advertiser_management/report_estimate.html'
    model = Ad

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads'] = Ad.objects.all()
        return context


class CTRListView(ListView):
    template_name = 'advertiser_management/report_ctr.html'
    model = Ad

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        start_time = self.kwargs['start_time']
        end_time = self.kwargs['end_time']
        ads = Ad.get_total_ctr(start_time, end_time)
        context['ads'] = ads
        return context


class TotalClicksAndViewsListView(ListView):
    template_name = 'advertiser_management/reports.html'
    model = Ad

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        start_time = self.kwargs['start_time']
        end_time = self.kwargs['end_time']
        delta = self.kwargs['delta']
        ads = Ad.get_total_clicks_views(start_time, end_time, delta)
        context['ads'] = ads
        return context


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
