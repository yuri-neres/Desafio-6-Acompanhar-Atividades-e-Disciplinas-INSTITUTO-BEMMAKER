from django.shortcuts import render
from core.decorators import aluno_required

# Create your views here.
@aluno_required
def index_aluno(request):
    return render(request, 'alunos/index.html')