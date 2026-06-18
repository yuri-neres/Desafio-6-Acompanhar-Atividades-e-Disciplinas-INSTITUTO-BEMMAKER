from django.urls import path
from . import views

urlpatterns = [
    # Rota institucional/página base
    path('', views.base, name="base"),
    
    # Tela inicial pós-login
    path('dashboard/', views.home_coordenacao, name='home_coordenacao'),
    
    # Módulo Acadêmico (Alunos)
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('alunos/novo/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/editar/<int:pk>/', views.editar_aluno, name='editar_aluno'),
    
    # Módulo de Atividades
    path('atividades/', views.lista_atividades, name='lista_atividades'),
    path('atividades/nova/', views.cadastrar_atividade, name='cadastrar_atividade'),
    path('atividades/editar/<int:pk>/', views.editar_atividade, name='editar_atividade'),
]