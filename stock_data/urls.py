from django.urls import path
from . import views

urlpatterns = [
    path('stocks/', views.get_multiple_stocks, name='get_multiple_stocks'),
]