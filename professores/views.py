from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from academico.models import Turma

@login_required
def index_professor(request):
    if not hasattr(request.user, 'perfil_professor'):
        messages.error(request, "Acesso negado. Área exclusiva para professores.")
        return redirect('home')
        
    prof_logado = request.user.perfil_professor
    
    turmas = Turma.objects.filter(professor=prof_logado)
    
    contexto = {
        'turmas': turmas
    }
        
    return render(request, 'professores/index.html', contexto)