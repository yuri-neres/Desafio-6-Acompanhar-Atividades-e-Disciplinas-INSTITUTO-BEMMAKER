from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

#from .models import Aluno, Atividade, Disciplina  
#from .forms import AlunoForm, AtividadeForm    

@login_required
def base(request):
    return render(request, 'core/base.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home_coordenacao')  
        else:
            return render(request, 'core/login.html', {
                'erro': 'Usuário ou senha incorretos. Tente novamente.'
            })

    return render(request, 'core/login.html')
# =========================================================================
# TELA INICIAL PÓS-LOGIN (DASHBOARD COORDENAÇÃO)
# =========================================================================

@login_required
def home_coordenacao(request):
    """Exibe o painel gerencial pedagógico com contadores em tempo real"""
    return render(request, 'core/home_coordenacao.html')
    # context = {
    #     'total_alunos': Aluno.objects.count(),
    #     'total_disciplinas': Disciplina.objects.count(),
    #     'total_atividades': Atividade.objects.count(),
    # }
    # return render(request, 'core/home_coordenacao.html', context)



# =========================================================================
# MÓDULO ACADÊMICO (GESTÃO DE ALUNOS)
# =========================================================================

# @login_required
# def lista_alunos(request):
#     """Lista todos os alunos para controle da coordenação"""
#     alunos = Aluno.objects.all()
#     return render(request, 'core/lista_alunos.html', {'alunos': alunos})

@login_required
def cadastrar_aluno(request):
    return render(request, 'core/cadastrar_aluno.html')
#     """Formulário de cadastro de novos estudantes para apoio à permanência"""
#     if request.method == 'POST':
#         form = AlunoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_alunos')
#     else:
#         form = AlunoForm()
#     return render(request, 'core/aluno_form.html', {'form': form, 'titulo': 'Cadastrar Aluno'})

# @login_required
# def editar_aluno(request, pk):
#     """Edita os dados cadastrais de um aluno existente através do ID (pk)"""
#     aluno = get_object_or_404(Aluno, pk=pk)
#     if request.method == 'POST':
#         form = AlunoForm(request.POST, instance=aluno)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_alunos')
#     else:
#         form = AlunoForm(instance=aluno)
#     return render(request, 'core/aluno_form.html', {'form': form, 'titulo': 'Editar Aluno'})


# # =========================================================================
# # MÓDULO DE ATIVIDADES (ACOMPANHAMENTO DIÁRIO)
# # =========================================================================

# @login_required
# def lista_atividades(request):
#     """Lista as atividades e prazos criados no sistema"""
#     atividades = Atividade.objects.all()
#     return render(request, 'core/lista_atividades.html', {'atividades': atividades})

@login_required
def cadastrar_atividade(request):
    return render(request, 'core/cadastrar_atividade.html') # será substituído após criação de models
#     """Permite à coordenação estipular novos prazos e tarefas"""
#     if request.method == 'POST':
#         form = AtividadeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_atividades')
#     else:
#         form = AtividadeForm()
#     return render(request, 'core/atividade_form.html', {'form': form, 'titulo': 'Criar Nova Atividade'})

# @login_required
# def editar_atividade(request, pk):
#     """Permite alterar prazos ou instruções de uma atividade específica"""
#     atividade = get_object_or_404(Atividade, pk=pk)
#     if request.method == 'POST':
#         form = AtividadeForm(request.POST, instance=atividade)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_atividades')
#     else:
#         form = AtividadeForm(instance=atividade)
#     return render(request, 'core/atividade_form.html', {'form': form, 'titulo': 'Editar Atividade'})

#========================================================================
# MÓDULO ACADÊMICO (GESTÃO DE PROFESSORES)
#========================================================================

@login_required
def cadastrar_professor(request):
    return render(request, 'core/cadastrar_professor.html') # será substituído após criação de models


# #=========================================================================
# # MÓDULO ACADÊMICO (ACOMPANHAMENTO DE TURMAS)
# #=========================================================================

login_required
def cadastrar_turma(request):
    return render(request, 'core/cadastrar_turma.html') # será substituído após criação de models

#=========================================================================
# MÓDULO ACADÊMICO (GESTÃO DE DISCIPLINAS)
#=========================================================================
@login_required
def cadastrar_disciplina(request):
    return render(request, 'core/cadastrar_disciplina.html') # será substituído após criação de models