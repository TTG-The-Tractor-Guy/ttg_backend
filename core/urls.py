# core/urls.py
from django.urls import path
from core.views import test_view, self_register

urlpatterns = [
    path('test/', test_view, name='core_demo'),
    path('self_register', self_register, name='customer_self_register'),
]