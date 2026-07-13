from django.contrib import admin
from .models import Atividade

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'disciplina', 'data_entrega')