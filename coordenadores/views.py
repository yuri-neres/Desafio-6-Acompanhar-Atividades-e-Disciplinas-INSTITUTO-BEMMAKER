from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from alunos.models import Aluno
from professores.models import Professor
from academico.models import Disciplina, Turma, Matricula
from django.contrib.auth.models import User

@login_required
def index_coordenacao(request):
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, "Acesso restrito à Coordenação Acadêmica.")
        return redirect('home')
        
    total_alunos = Aluno.objects.count()
    total_professores = Professor.objects.count()
    total_disciplinas = Disciplina.objects.count()
    total_turmas = Turma.objects.count()
    
    contexto = {
        'total_alunos': total_alunos,
        'total_professores': total_professores,
        'total_disciplinas': total_disciplinas,
        'total_turmas': total_turmas,
    }
    
    return render(request, 'coordenadores/index.html', contexto)

@login_required
def gerenciar_disciplinas(request):
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, "Acesso restrito.")
        return redirect('home')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        codigo = request.POST.get('codigo')
        carga_horaria = request.POST.get('carga_horaria')
        descricao = request.POST.get('descricao')
        
        try:
            Disciplina.objects.create(
                nome=nome,
                codigo=codigo,
                carga_horaria=carga_horaria,
                descricao=descricao
            )
        except:
            pass 
            
        return redirect('coordenadores:disciplinas')

    disciplinas = Disciplina.objects.all().order_by('nome')
    
    contexto = {
        'disciplinas': disciplinas
    }
    return render(request, 'coordenadores/disciplinas.html', contexto)

@login_required
def editar_disciplina(request, id_disciplina):
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, "Acesso restrito.")
        return redirect('home')

    disciplina = get_object_or_404(Disciplina, id=id_disciplina)

    if request.method == 'POST':
        disciplina.nome = request.POST.get('nome')
        disciplina.codigo = request.POST.get('codigo')
        disciplina.carga_horaria = request.POST.get('carga_horaria')
        disciplina.descricao = request.POST.get('descricao')
        disciplina.save()
        messages.success(request, "Disciplina atualizada com sucesso!")
        return redirect('coordenadores:disciplinas')

    contexto = {'disciplina': disciplina}
    return render(request, 'coordenadores/editar_disciplina.html', contexto)

@login_required
def excluir_disciplina(request, id_disciplina):
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, "Acesso restrito.")
        return redirect('home')

    disciplina = get_object_or_404(Disciplina, id=id_disciplina)
    disciplina.delete()
    messages.success(request, "Disciplina excluída com sucesso!")
    return redirect('coordenadores:disciplinas')

@login_required
def gerenciar_turmas(request):
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, "Acesso restrito.")
        return redirect('home')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        disciplina_id = request.POST.get('disciplina_id')
        professor_id = request.POST.get('professor_id')
        ano = request.POST.get('ano') or 2026
        semestre = request.POST.get('semestre') or 1
        
        disciplina = get_object_or_404(Disciplina, id=disciplina_id)
        professor = Professor.objects.filter(id=professor_id).first() if professor_id else None
        
        Turma.objects.create(
            nome=nome,
            disciplina=disciplina,
            professor=professor,
            ano=ano,
            semestre=semestre
        )
        
        return redirect('coordenadores:turmas')

    turmas = Turma.objects.select_related('disciplina', 'professor__usuario').all().order_by('-ano', '-semestre', 'nome')
    disciplinas = Disciplina.objects.all().order_by('nome')
    professores = Professor.objects.select_related('usuario').all()
    
    contexto = {
        'turmas': turmas,
        'disciplinas': disciplinas,
        'professores': professores,
    }
    return render(request, 'coordenadores/turmas.html', contexto)

@login_required
def editar_turma(request, id_turma):
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, "Acesso restrito.")
        return redirect('home')

    turma = get_object_or_404(Turma, id=id_turma)

    if request.method == 'POST':
        turma.nome = request.POST.get('nome')
        disciplina_id = request.POST.get('disciplina_id')
        professor_id = request.POST.get('professor_id')
        turma.ano = request.POST.get('ano')
        turma.semestre = request.POST.get('semestre')

        turma.disciplina = get_object_or_404(Disciplina, id=disciplina_id)
        turma.professor = Professor.objects.filter(id=professor_id).first() if professor_id else None
        turma.save()

        messages.success(request, "Turma/Alocação atualizada com sucesso!")
        return redirect('coordenadores:turmas')

    disciplinas = Disciplina.objects.all().order_by('nome')
    professores = Professor.objects.select_related('usuario').all()

    contexto = {
        'turma': turma,
        'disciplinas': disciplinas,
        'professores': professores
    }
    return render(request, 'coordenadores/editar_turma.html', contexto)

@login_required
def excluir_turma(request, id_turma):
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, "Acesso restrito.")
        return redirect('home')

    turma = get_object_or_404(Turma, id=id_turma)
    turma.delete()
    messages.success(request, "Turma excluída com sucesso!")
    return redirect('coordenadores:turmas')

@login_required
def gerenciar_matriculas(request):
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, "Acesso restrito.")
        return redirect('home')

    if request.method == 'POST':
        aluno_id = request.POST.get('aluno_id')
        turma_id = request.POST.get('turma_id')
        
        aluno = get_object_or_404(Aluno, id=aluno_id)
        turma = get_object_or_404(Turma, id=turma_id)
        
        Matricula.objects.get_or_create(
            aluno=aluno,
            turma=turma,
            defaults={'ativo': True}
        )
        
        messages.success(request, "Matrícula realizada com sucesso!")
        return redirect('coordenadores:matriculas')

    matriculas = Matricula.objects.select_related('aluno__usuario', 'turma__disciplina').all().order_by('-data_matricula')
    alunos = Aluno.objects.select_related('usuario').all().order_by('usuario__first_name')
    turmas = Turma.objects.select_related('disciplina').all().order_by('-ano', '-semestre', 'nome')
    
    contexto = {
        'matriculas': matriculas,
        'alunos': alunos,
        'turmas': turmas
    }
    return render(request, 'coordenadores/matriculas.html', contexto)

@login_required
def gerenciar_usuarios(request):
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, "Acesso restrito.")
        return redirect('home')

    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        identificacao = request.POST.get('identificacao') # Matrícula (Aluno) ou Titulação (Professor)

        if User.objects.filter(username=username).exists():
            messages.error(request, "Erro: Este nome de usuário já está em uso.")
            return redirect('coordenadores:usuarios')

        try:
            # 1. Cria a conta de acesso nativa do Django
            novo_usuario = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )

            # 2. Cria o perfil correspondente e vincula à conta
            if tipo == 'aluno':
                Aluno.objects.create(usuario=novo_usuario, matricula_curso=identificacao)
            elif tipo == 'professor':
                Professor.objects.create(usuario=novo_usuario, titulacao=identificacao)
                
            messages.success(request, f"{tipo.capitalize()} cadastrado com sucesso!")
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar usuário: {e}")

        return redirect('coordenadores:usuarios')

    alunos = Aluno.objects.select_related('usuario').all().order_by('usuario__first_name')
    professores = Professor.objects.select_related('usuario').all().order_by('usuario__first_name')
    
    contexto = {
        'alunos': alunos,
        'professores': professores
    }
    return render(request, 'coordenadores/usuarios.html', contexto)