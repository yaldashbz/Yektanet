from django.urls import path, register_converter, include

from advertiser_management.views.old_views import EstimateDurationListView, CTRListView, TotalClicksAndViewsListView, \
    ShowAllAdsListView, CreateAdFormView
from advertiser_management.views.user_views import AdOnClickRedirectView, AdViewSet
from advertiser_management.views.report_views import ReportViewSet
from advertiser_management.converters import DateTimeConverter
from rest_framework.routers import DefaultRouter


register_converter(DateTimeConverter, 'date-time')

router = DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-ad/',
         CreateAdFormView.as_view()),
    path('all-ads/',
         ShowAllAdsListView.as_view()),
    path('click/<int:ad_id>/',
         AdOnClickRedirectView.as_view()),
    path('report/start=<date-time:start_time>&end=<date-time:end_time>&delta=<int:delta>/',
         TotalClicksAndViewsListView.as_view()),
    path('report-csr/start=<date-time:start_time>&end=<date-time:end_time>/',
         CTRListView.as_view()),
    path('report-estimate/',
         EstimateDurationListView.as_view())
]
