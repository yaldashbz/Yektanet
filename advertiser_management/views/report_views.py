from django.views.generic.list import ListView
from django.db.models import Count, Q, F, FloatField
from django.db.models.functions import Cast
from django.utils import timezone

from advertiser_management.models import Ad


class EstimateDurationListView(ListView):
    template_name = 'advertiser_management/report_estimate.html'
    model = Ad

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads'] = Ad.objects.all()
        return context


class CSRListView(ListView):
    template_name = 'advertiser_management/report_csr.html'
    model = Ad

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        start_time = self.kwargs['start_time']
        end_time = self.kwargs['end_time']
        ads = get_ads_total_csr(start_time, end_time)
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
        ads = get_ads_total_clicks_views(start_time, end_time, delta)
        context['ads'] = ads
        return context


def get_ads_total_csr(start_time, end_time):
    return Ad.objects.annotate(
        csr=Cast(Count(
            F('clicks'),
            distinct=True,
            filter=Q(
                clicks__time__range=(start_time, end_time)
            )
        ), FloatField()) / Cast(Count(
            F('views'),
            distinct=True,
            filter=Q(
                views__time__range=(start_time, end_time)
            ),
            output_field=FloatField()
        ), FloatField())
    ).order_by('-csr')


def get_ads_total_clicks_views(start_time, end_time, delta):
    ads = Ad.objects.all()
    response = dict()
    for ad in ads:
        ad_response = list()
        start = start_time
        while start < end_time:
            end = start + timezone.timedelta(hours=delta)
            d = get_query(ad, start_time=start, end_time=end)
            ad_response.append(d)

            start = end

        response.update({ad: ad_response})

    return response


def get_query(ad, start_time, end_time):
    clicks_count = ad.clicks.filter(
        time__range=(start_time, end_time)
    ).count()

    views_count = ad.views.filter(
        time__range=(start_time, end_time)
    ).count()

    d = dict()
    d.update({
        'start_time': start_time,
        'end_time': end_time,
        'total_clicks': clicks_count,
        'total_view': views_count,
    })
    return d
