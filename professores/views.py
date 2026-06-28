from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from .models import Professor  
from .forms import ProfessorForm   


@login_required
def cadastrar_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_professores')

    else:
        form = ProfessorForm()

    return render(
        request,
        'core/professor_form.html',
        {
            'form': form,
            'titulo': 'Cadastrar Professor'
        }
    )
