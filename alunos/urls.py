from django.urls import path
from . import views

app_name = 'alunos'

urlpatterns = [
    path('', views.index_aluno, name = "index"),
    path('disciplinas/', views.disciplinas, name="disciplinas"),
    path('sala/<int:id_turma>/', views.sala_virtual, name="sala_virtual"),
]