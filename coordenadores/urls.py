from django.urls import path
from . import views

app_name = 'coordenadores'

urlpatterns = [
    path('', views.index_coordenacao, name="index"),
    path('disciplinas/', views.gerenciar_disciplinas, name="disciplinas"),
    path('disciplinas/editar/<int:id_disciplina>/', views.editar_disciplina, name="editar_disciplina"),
    path('disciplinas/excluir/<int:id_disciplina>/', views.excluir_disciplina, name="excluir_disciplina"),
    path('turmas/', views.gerenciar_turmas, name="turmas"),
    path('turmas/editar/<int:id_turma>/', views.editar_turma, name="editar_turma"),
    path('turmas/excluir/<int:id_turma>/', views.excluir_turma, name="excluir_turma"),
    path('matriculas/', views.gerenciar_matriculas, name="matriculas"),
    path('usuarios/', views.gerenciar_usuarios, name="usuarios"),
]