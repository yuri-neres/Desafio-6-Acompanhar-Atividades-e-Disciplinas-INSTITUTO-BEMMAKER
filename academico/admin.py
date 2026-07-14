from django.contrib import admin
from .models import Disciplina, Turma, Matricula, Atividade, EntregaAtividade, Aula, Presenca, Avaliacao, Nota

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'codigo', 'carga_horaria']
    search_fields = ['nome', 'codigo']

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'disciplina', 'professor', 'ano', 'semestre']
    list_filter = ['ano', 'semestre', 'disciplina']
    search_fields = ['nome']

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'turma', 'data_matricula', 'ativo']
    list_filter = ['ativo', 'turma']
    search_fields = ['aluno__usuario__first_name', 'aluno__matricula']

# Registros simples para os demais modelos operacionais
admin.site.register(Atividade)
admin.site.register(EntregaAtividade)
admin.site.register(Aula)
admin.site.register(Presenca)
admin.site.register(Avaliacao)
admin.site.register(Nota)