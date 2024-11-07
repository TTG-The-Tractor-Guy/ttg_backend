# core/urls.py
from django.urls import path
from core.views import test_view, sign_up

urlpatterns = [
    path('/profile', test_view, name='Get my profile'),
    path('/sign_up', sign_up, name='Get my profile'),
]


