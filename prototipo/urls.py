from django.urls import path
from .views import index, tweets, estatisticas, mapa

urlpatterns = [
    path('', index),
    path('tweets', tweets),
    path('estatisticas', estatisticas),
    path('mapa', mapa),
]