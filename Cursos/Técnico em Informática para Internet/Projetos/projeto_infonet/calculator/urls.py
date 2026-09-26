from django.urls import path
from . import views

app_name = 'calculator'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/calculate/', views.calculate, name='calculate'),
    path('api/history/', views.history, name='history'),
    path('api/history/clear/', views.clear_history, name='clear_history'),
]
