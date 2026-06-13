from django.urls import path
from .views import home

app_name = 'coordenadores'

urlpatterns = [
    path("", home),
]