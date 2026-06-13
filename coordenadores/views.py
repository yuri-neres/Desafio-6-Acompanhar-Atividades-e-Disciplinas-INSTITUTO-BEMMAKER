from django.shortcuts import render
#from datetime import date
from .models import Coordenador
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, Coordenadores!")
    c = Coordenador.objects.get(id=1)
    contexto = {"coordenadores": c}
    return render(request, 'home.html', contexto)