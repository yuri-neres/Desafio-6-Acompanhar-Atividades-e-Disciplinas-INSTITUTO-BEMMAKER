# coordenadores/urls.py
from django.urls import path
from . import views

app_name = 'coordenadores'

urlpatterns = [
    path('', views.index, name='index'),
]