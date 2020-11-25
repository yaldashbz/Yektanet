from django.urls import path
from advertiser_management.views import AdOnClickRedirectView, CreateAdFormView, ShowAllAdsListView

urlpatterns = [
    path('create-ad/', CreateAdFormView.as_view()),
    path('all-ads/', ShowAllAdsListView.as_view()),
    path('click/<int:ad_id>/', AdOnClickRedirectView.as_view())
]
