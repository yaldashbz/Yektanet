from django.urls import path
from . import views

urlpatterns = [
    path('create-ad/', views.create_ad, name='create-ad'),
    path('all-ads/', views.show_ads_all, name='all-ads'),
    path('click/<int:ad_id>/', views.AdOnClickRedirectView.as_view(), name='ad_on_click')
]
