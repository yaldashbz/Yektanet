from django.urls import path, register_converter
from advertiser_management.views.user_views import AdOnClickRedirectView, CreateAdFormView, ShowAllAdsListView
from advertiser_management.views.report_views import TotalClicksAndViewsListView, CSRListView, EstimateDurationListView
from advertiser_management.converters import DateTimeConverter

register_converter(DateTimeConverter, 'date-time')

urlpatterns = [
    path('create-ad/',
         CreateAdFormView.as_view()),
    path('all-ads/',
         ShowAllAdsListView.as_view()),
    path('click/<int:ad_id>/',
         AdOnClickRedirectView.as_view()),
    path('report/start=<date-time:start_time>&end=<date-time:end_time>&delta=<int:delta>/',
         TotalClicksAndViewsListView.as_view()),
    path('report-csr/start=<date-time:start_time>&end=<date-time:end_time>/',
         CSRListView.as_view()),
    path('report-estimate/', EstimateDurationListView.as_view())
]
