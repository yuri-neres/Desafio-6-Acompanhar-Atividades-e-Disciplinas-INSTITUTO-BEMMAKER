from django import forms
from .models import Aluno, Professor, Disciplina, Atividade

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        # IMPORTANTE: Alinhar esses nomes com os campos que seu colega criou no models.py
        fields = ['nome', 'email', 'matricula', 'turma', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex: nome@email.com'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número da matrícula'}),
            'turma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Turma do aluno'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: (11) 99999-9999'}),
        }

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'codigo', 'professor_orientador', 'carga_horaria']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'professor_orientador': forms.Select(attrs={'class': 'form-control'}),
            'carga_horaria': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['titulo', 'descricao', 'disciplina', 'data_prazo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da atividade'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descrição das instruções...'}),
            'disciplina': forms.Select(attrs={'class': 'form-control'}),
            'data_prazo': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }