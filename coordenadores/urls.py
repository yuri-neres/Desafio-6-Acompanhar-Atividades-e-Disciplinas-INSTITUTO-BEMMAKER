from django.urls import path
from . import views

urlpatterns = [
     path('cadastrar/', views.cadastrar_coordenador, name='cadastrar_coordenador'),
#    path('turmas/', views.lista_turmas, name='lista_turmas'),
     path('turmas/nova/', views.cadastrar_turma, name='cadastrar_turma'),
#    path('turmas/editar/<int:pk>/', views.editar_turma, name='editar_turma'),
]
