from django.urls import path
from .views import days

urlpatterns = [
    path('', days, name='home'),
]
