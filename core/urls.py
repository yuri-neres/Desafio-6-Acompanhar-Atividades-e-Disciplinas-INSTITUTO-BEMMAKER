from django.urls import path
from . import views
from .views import base, login, home_coordenacao, cadastrar_aluno, cadastrar_professor, cadastrar_disciplina, cadastrar_atividade, cadastrar_turma

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


    # Módulo Acadêmico (Professores)
#    path('professores/', views.lista_professores, name='lista_professores'),
     path('professores/novo/', views.cadastrar_professor, name='cadastrar_professor'),
#    path('professores/editar/<int:pk>/', views.editar_professor, name='editar_professor'),

#   # Módulo Acadêmico (Disciplinas)
#    path('disciplinas/', views.lista_disciplinas, name='lista_disciplinas'),
     path('disciplinas/nova/', views.cadastrar_disciplina, name='cadastrar_disciplina'),
#    path('disciplinas/editar/<int:pk>/', views.editar_disciplina, name='editar_disciplina'),       

    # Módulo Acadêmico (Turmas)
#    path('turmas/', views.lista_turmas, name='lista_turmas'),
     path('turmas/nova/', views.cadastrar_turma, name='cadastrar_turma'),
#    path('turmas/editar/<int:pk>/', views.editar_turma, name='editar_turma'),
]
