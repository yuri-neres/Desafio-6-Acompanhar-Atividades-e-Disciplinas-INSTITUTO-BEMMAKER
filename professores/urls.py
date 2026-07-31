from django.urls import path
from . import views

app_name = 'professores'

urlpatterns = [
    path('', views.index_professor, name='index'),
    path('turma/<int:id_turma>/', views.gerenciar_turma, name="gerenciar_turma"),
]