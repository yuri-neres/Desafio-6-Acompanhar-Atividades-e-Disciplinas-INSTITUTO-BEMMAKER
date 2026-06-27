from django.contrib import admin
from .models import Coordenador

@admin.register(Coordenador)
class CoordenadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'setor', 'email', 'telefone')
    search_fields = ('nome', 'email')