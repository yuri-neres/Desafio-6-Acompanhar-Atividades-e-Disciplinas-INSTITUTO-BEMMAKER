from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from academico.models import Turma, Aula, Atividade, Avaliacao, Nota, Matricula, Presenca

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


@login_required
def gerenciar_turma(request, id_turma):
    if not hasattr(request.user, 'perfil_professor'):
        messages.error(request, "Acesso negado.")
        return redirect('home')
        
    prof_logado = request.user.perfil_professor
    turma = get_object_or_404(Turma, id=id_turma, professor=prof_logado)
    
    if request.method == 'POST':
        acao = request.POST.get('acao')
        
        # 1. Cadastro de Aula
        if acao == 'criar_aula':
            data_aula = request.POST.get('data')
            conteudo = request.POST.get('conteudo_ministrado')
            Aula.objects.create(
                turma=turma,
                data=data_aula,
                conteudo_ministrado=conteudo
            )
            
        # 2. Cadastro de Atividade
        elif acao == 'criar_atividade':
            titulo = request.POST.get('titulo')
            descricao = request.POST.get('descricao')
            data_entrega = request.POST.get('data_entrega')
            nota_maxima = request.POST.get('nota_maxima') or 10.0
            
            Atividade.objects.create(
                turma=turma,
                titulo=titulo,
                descricao=descricao,
                data_entrega=data_entrega,
                nota_maxima=nota_maxima
            )

        # 3. Cadastro de Avaliação Formal
        elif acao == 'criar_avaliacao':
            nome = request.POST.get('nome')
            peso = request.POST.get('peso') or 1.0
            nota_maxima = request.POST.get('nota_maxima') or 10.0
            
            Avaliacao.objects.create(
                turma=turma,
                nome=nome,
                peso=peso,
                nota_maxima=nota_maxima
            )

        # 4. Lançamento de Notas
        elif acao == 'salvar_notas':
            avaliacao_id = request.POST.get('avaliacao_id')
            avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id, turma=turma)
            
            matriculas = Matricula.objects.filter(turma=turma, ativo=True)
            
            for m in matriculas:
                campo_nota = f"nota_aluno_{m.aluno.id}"
                valor = request.POST.get(campo_nota)
                
                if valor is not None and valor != '':
                    Nota.objects.update_or_create(
                        avaliacao=avaliacao,
                        aluno=m.aluno,
                        defaults={'valor_nota': valor}
                    )

        # 5. Registro de Frequência (Chamada)
        elif acao == 'salvar_frequencia':
            aula_id = request.POST.get('aula_id')
            aula = get_object_or_404(Aula, id=aula_id, turma=turma)
            
            matriculas = Matricula.objects.filter(turma=turma, ativo=True)
            
            for m in matriculas:
                campo_presenca = f"presenca_aluno_{m.aluno.id}"
                # Se o checkbox estiver marcado na requisição, ele enviará valor no POST
                esta_presente = campo_presenca in request.POST
                
                Presenca.objects.update_or_create(
                    aula=aula,
                    aluno=m.aluno,
                    defaults={'presente': esta_presente}
                )
        
        return redirect('professores:gerenciar_turma', id_turma=turma.id)
        
    aulas_postadas = Aula.objects.filter(turma=turma).order_by('-data')
    atividades_cadastradas = Atividade.objects.filter(turma=turma).order_by('data_entrega')
    avaliacoes = Avaliacao.objects.filter(turma=turma)
    matriculas_ativas = Matricula.objects.filter(turma=turma, ativo=True).select_related('aluno__usuario')
    
    contexto = {
        'turma': turma,
        'aulas': aulas_postadas,
        'atividades': atividades_cadastradas,
        'avaliacoes': avaliacoes,
        'matriculas': matriculas_ativas,
    }
    return render(request, 'professores/gerenciar_turma.html', contexto)