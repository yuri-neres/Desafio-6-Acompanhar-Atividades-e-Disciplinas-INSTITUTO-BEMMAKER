# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home_view(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'perfil_aluno'):
            return redirect('alunos:index')
        elif hasattr(request.user, 'perfil_professor'):
            return redirect('professores:index')
        elif hasattr(request.user, 'perfil_coordenador'):
            return redirect('coordenadores:index')
        elif request.user.is_superuser:
            return redirect('admin:index')
            
    return render(request, 'home.html') 

def logout_view(request):
    logout(request)
    return redirect('home')