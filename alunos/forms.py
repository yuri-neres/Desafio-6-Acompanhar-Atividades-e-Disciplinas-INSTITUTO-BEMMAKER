from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        # IMPORTANTE: Alinhar esses nomes com os campos que seu colega criou no models.py
        model = Aluno
        fields = ['nome', 'serie', 'periodo', 'telefone', 'email']

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome completo'}),
            'serie': forms.TextInput(attrs={'placeholder': 'Ex: 1º Ano'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(11) 99999-9999'}),
            'email': forms.EmailInput(attrs={'placeholder': 'nome@email.com'}),
            }

# class DisciplinaForm(forms.ModelForm):
#     class Meta:
#         model = Disciplina
#         fields = ['nome', 'codigo', 'professor_orientador', 'carga_horaria']
#         widgets = {
#             'nome': forms.TextInput(attrs={'class': 'form-control'}),
#             'codigo': forms.TextInput(attrs={'class': 'form-control'}),
#             'professor_orientador': forms.Select(attrs={'class': 'form-control'}),
#             'carga_horaria': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

# class AtividadeForm(forms.ModelForm):
#     class Meta:
#         model = Atividade
#         fields = ['titulo', 'descricao', 'disciplina', 'data_prazo']
#         widgets = {
#             'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da atividade'}),
#             'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descrição das instruções...'}),
#             'disciplina': forms.Select(attrs={'class': 'form-control'}),
#             'data_prazo': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#         }

# class ProfessorForm(forms.ModelForm):
#     class Meta:
#         model = Professor
#         fields = ['nome', 'email', 'telefone', 'disciplina']
#         widgets = {
#             'nome': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nome completo'}),
#             'matricula': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Número da matrícula'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Ex: professor@email.com'}),
#             'telefone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex: (11) 99999-9999'}),
#             'disciplina': forms.Select(attrs={'class': 'form-control'}),
#         }

# class TurmaForm(forms.ModelForm):
#     class Meta:
#         model = Turma
#         fields = ['nome', 'codigo', 'turno']
#         widgets = {
#             'nome': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nome da turma'}),
#             'codigo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex: TDS-2026-A'}),
#             'turno': forms.Select(attrs={'class': 'form-control'}),
#         }