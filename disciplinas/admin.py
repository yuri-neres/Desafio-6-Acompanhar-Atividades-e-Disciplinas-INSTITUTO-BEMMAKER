from django.contrib import admin
from .models import Disciplina

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'professor')
    search_fields = ('nome',)