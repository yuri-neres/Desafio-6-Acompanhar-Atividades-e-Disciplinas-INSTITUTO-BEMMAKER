from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from academico.models import Matricula, Aula, Atividade, Nota

@login_required
def index_aluno(request):
    if not hasattr(request.user, 'perfil_aluno'):
        messages.error(request, "Você não tem permissão para acessar esta página. Área exclusiva para alunos.")
        return redirect('home')
        
    aluno_logado = request.user.perfil_aluno
    
    matriculas = Matricula.objects.filter(aluno=aluno_logado, ativo=True).select_related('turma__disciplina', 'turma__professor')
    
    contexto = {
        'matriculas': matriculas
    }
        
    return render(request, 'alunos/index.html', contexto)

@login_required
def disciplinas(request):
    if not hasattr(request.user, 'perfil_aluno'):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('home')
        
    aluno_logado = request.user.perfil_aluno
    matriculas = Matricula.objects.filter(aluno=aluno_logado, ativo=True).select_related('turma__disciplina', 'turma__professor')
    
    contexto = {
        'matriculas': matriculas
    }

    return render(request, 'alunos/disciplinas.html', contexto)

@login_required
def sala_virtual(request, id_turma):
    if not hasattr(request.user, 'perfil_aluno'):
        messages.error(request, "Acesso negado.")
        return redirect('home')
        
    aluno_logado = request.user.perfil_aluno
    matricula = get_object_or_404(Matricula, aluno=aluno_logado, turma_id=id_turma, ativo=True)
    turma = matricula.turma
    
    aulas = Aula.objects.filter(turma=turma).order_by('-data')
    atividades = Atividade.objects.filter(turma=turma).order_by('data_entrega')
    
    notas = Nota.objects.filter(aluno=aluno_logado, avaliacao__turma=turma)
    
    contexto = {
        'turma': turma,
        'aulas': aulas,
        'atividades': atividades,
        'notas': notas
    }
        
    return render(request, 'alunos/sala_virtual.html', contexto)