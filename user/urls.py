from django.urls import path

from user.views import LoginView, RegisterView, CustomerListView, UserListView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('customers/', CustomerListView.as_view()),
    path('users/', UserListView.as_view())
]
