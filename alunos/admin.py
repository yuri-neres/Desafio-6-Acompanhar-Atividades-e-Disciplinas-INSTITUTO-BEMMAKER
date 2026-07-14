from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    # Mostra os campos que realmente existem no nosso novo models.py
    list_display = ['usuario', 'matricula', 'cpf', 'telefone']
    
    # Permite pesquisar pelo nome do usuário, matrícula ou cpf
    search_fields = ['usuario__first_name', 'usuario__last_name', 'matricula', 'cpf']