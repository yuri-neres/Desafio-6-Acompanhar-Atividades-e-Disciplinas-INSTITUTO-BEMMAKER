from django.urls import path
from . import views

app_name = 'professores'

urlpatterns = [
    path('', views.index_professor, name='index'),
]