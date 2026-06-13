from django.shortcuts import render
from datetime import date
from .models import Aluno
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, Django!")
    a = Aluno.objects.get(id=1)
    contexto = {"alunos": a}
    return render(request, 'home.html', contexto)