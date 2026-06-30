from django import forms
from .models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'especialidade', 'telefone', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nome completo'}),
            'especialidade': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Especialidade'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex: (11) 99999-9999'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Ex: professor@email.com'}),
        }