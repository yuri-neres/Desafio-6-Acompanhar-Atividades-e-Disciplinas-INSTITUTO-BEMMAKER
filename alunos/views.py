from django.shortcuts import render

# Create your views here.
def index_aluno(request):
    return render(request, 'alunos/index.html')