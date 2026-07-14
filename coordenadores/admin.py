from django.contrib import admin
from .models import Coordenador

@admin.register(Coordenador)
class CoordenadorAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'registro_coordenacao', 'telefone']
    search_fields = ['usuario__first_name', 'usuario__last_name', 'registro_coordenacao']