from django.urls import path
from .views import days, tbl_month

urlpatterns = [
    path('', days, name='home'),
    path('month/<slug:slug>/', tbl_month, name='tbl_month'),
]
