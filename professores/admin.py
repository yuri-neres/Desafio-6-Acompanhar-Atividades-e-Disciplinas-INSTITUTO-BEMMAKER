from django.contrib import admin
from .models import Professor

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    #Config do admin para o model Professor
    list_display = ['nome', 'email', 'telefone', 'cpf', 'ativo', 'data_criacao']
    list_display_links = ['nome']
    list_filter = ['ativo', 'data_criacao', 'data_nascimento']
    search_fields = ['nome', 'email', 'cpf', 'telefone']
    list_per_page = 25
    list_editable = ['ativo']
    ordering = ['-data_criacao']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'email', 'telefone')
        }),
        ('Documentos', {
            'fields': ('cpf', 'data_nascimento')
        }),
        ('Endereço', {
            'fields': ('endereco',)
        }),
        ('Status', {
            'fields': ('ativo',)
        }),
        ('Datas', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['data_criacao', 'data_atualizacao']