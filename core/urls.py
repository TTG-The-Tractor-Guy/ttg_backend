# core/urls.py
from django.urls import path
from core.views import test_view

urlpatterns = [
    path('test/', test_view, name='core_demo'),
]