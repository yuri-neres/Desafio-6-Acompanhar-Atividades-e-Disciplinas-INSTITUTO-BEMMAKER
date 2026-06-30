from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CoordenadorForm

@login_required
def cadastrar_coordenador(request):
    if request.method == 'POST':
        form = CoordenadorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cadastrar_coordenador')  # ou outra página

    else:
        form = CoordenadorForm()

    return render(
        request,
        'coordenadores/coordenador_form.html',
        {
            'form': form,
            'titulo': 'Cadastrar Coordenador'
        }
    )

@login_required
def cadastrar_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cadastrar_turma')  # ou outra página

    else:
        form = TurmaForm()

    return render(
        request,
        'alunos/turma_form.html',
        {
            'form': form,
            'titulo': 'Cadastrar Turma'
        }
    )