from django import forms
from .models import Coordenador

class CoordenadorForm(forms.ModelForm):
    class Meta:
        model = Coordenador
        fields = ['nome', 'setor', 'telefone', 'email']

        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nome completo'}),
                   'telefone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex: (11) 99999-9999'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Ex: coordenador@email.com'}), 
        }

# class TurmaForm(forms.ModelForm):
#     class Meta:
#         model = Turma
#         fields = ['nome', 'codigo', 'turno']
#         widgets = {
#             'nome': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nome da turma'}),
#             'codigo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex: TDS-2026-A'}),
#             'turno': forms.Select(attrs={'class': 'form-control'}),
#         }