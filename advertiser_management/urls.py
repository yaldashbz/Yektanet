from django.urls import path, include

from advertiser_management.views.user_views import AdOnClickRedirectView, AdViewSet, ShowAllAdsListView
from advertiser_management.views.report_views import ReportViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all-ads/',
         ShowAllAdsListView.as_view()),
    path('click/<int:ad_id>/',
         AdOnClickRedirectView.as_view()),
]
