from django import forms
from .models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'email', 'telefone', 'disciplina']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nome completo'}),
            'especialidade': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Número da matrícula'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Ex: professor@email.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex: (11) 99999-9999'}),
        }