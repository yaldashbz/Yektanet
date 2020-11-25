from django.urls import path
from advertiser_management.views import create_ad, show_ads_all, AdOnClickRedirectView, CreateAdFormView

urlpatterns = [
    path('create-ad/', CreateAdFormView.as_view(), name='create-ad'),
    path('all-ads/', show_ads_all, name='all-ads'),
    path('click/<int:ad_id>/', AdOnClickRedirectView.as_view(), name='ad_on_click')
]
