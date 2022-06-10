from django.urls import path
from .views import days, tb_month

urlpatterns = [
    path('', days, name='home'),
    path('month/<slug:slug>/', tb_month, name='tb_month'),
]
