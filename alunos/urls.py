from django.urls import path
from . import views
from .views import base, login, home_coordenacao, cadastrar_aluno
from professores.views import cadastrar_professor

urlpatterns = [

    #  login como página inicial
    path('', views.login, name="login"),    

    # Rota institucional/página base
    path('home/', views.base, name="base"),
    
    # # Tela inicial pós-login
    path('dashboard/', views.home_coordenacao, name='home_coordenacao'),
    
    # Módulo Acadêmico (Alunos)
#    path('alunos/', views.lista_alunos, name='lista_alunos'),
     path('alunos/novo/', views.cadastrar_aluno, name='cadastrar_aluno'),
#    path('alunos/editar/<int:pk>/', views.editar_aluno, name='editar_aluno'),
    
#     # Módulo de Atividades
#     path('atividades/', views.lista_atividades, name='lista_atividades'),
      path('atividades/nova/', views.cadastrar_atividade, name='cadastrar_atividade'),
#     path('atividades/editar/<int:pk>/', views.editar_atividade, name='editar_atividade'),


    

#   # Módulo Acadêmico (Disciplinas)
#    path('disciplinas/', views.lista_disciplinas, name='lista_disciplinas'),
     path('disciplinas/nova/', views.cadastrar_disciplina, name='cadastrar_disciplina'),
#    path('disciplinas/editar/<int:pk>/', views.editar_disciplina, name='editar_disciplina'),       
]