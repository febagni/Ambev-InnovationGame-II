from django.urls import path
from .views import index, tweets, filtros

urlpatterns = [
    path('', tweets),
    path('tweets', tweets),
    path('filtros', filtros)
]