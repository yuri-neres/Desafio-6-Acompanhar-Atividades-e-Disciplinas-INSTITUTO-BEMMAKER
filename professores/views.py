from django.shortcuts import render
#from datetime import date
from .models import Professor
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, Professores!")
    p = Professor.objects.get(id=1)
    contexto = {"professores": p}
    return render(request, 'home.html', contexto)