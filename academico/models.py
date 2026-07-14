from django.db import models
from alunos.models import Aluno
from professores.models import Professor

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    carga_horaria = models.PositiveIntegerField(verbose_name="Carga Horária (Horas)")

    def __str__(self):
        return f"{self.nome} ({self.codigo})"


class Turma(models.Model):
    SEMESTRES = [
        (1, '1º Semestre'),
        (2, '2º Semestre'),
    ]
    nome = models.CharField(max_length=50, verbose_name="Identificação da Turma") # Ex: "Turma A - 2026"
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='turmas')
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, related_name='turmas')
    alunos = models.ManyToManyField(Aluno, through='Matricula', related_name='turmas')
    ano = models.PositiveIntegerField(default=2026, verbose_name="Ano Letivo")
    semestre = models.PositiveIntegerField(choices=SEMESTRES, verbose_name="Semestre")

    def __str__(self):
        return f"{self.nome} - {self.disciplina.nome}"


class Matricula(models.Model):
    """Tabela de associação entre Aluno e Turma para permitir histórico de matrículas"""
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas_turma')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_matricula = models.DateField(auto_now_add=True, verbose_name="Data de Matrícula")
    ativo = models.BooleanField(default=True, verbose_name="Matrícula Ativa")

    class Meta:
        unique_together = ('aluno', 'turma')

    def __str__(self):
        return f"{self.aluno} matriculado em {self.turma}"


class Atividade(models.Model):
    """Atividades e tarefas propostas pelo professor"""
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='atividades')
    titulo = models.CharField(max_length=150, verbose_name="Título da Atividade")
    descricao = models.TextField(verbose_name="Descrição da Tarefa")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    data_entrega = models.DateTimeField(verbose_name="Prazo Limite de Entrega")
    nota_maxima = models.DecimalField(max_digits=5, decimal_places=2, default=10.0, verbose_name="Nota Máxima")

    def __str__(self):
        return f"{self.titulo} | {self.turma.nome}"


class EntregaAtividade(models.Model):
    """Envio de resoluções por parte dos alunos e respectiva avaliação"""
    STATUS_ENTREGA = [
        ('pendente', 'Pendente de Correção'),
        ('entregue', 'Entregue no Prazo'),
        ('atrasado', 'Entregue com Atraso'),
        ('corrigido', 'Corrigido e Avaliado'),
    ]
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, related_name='entregas')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='entregas')
    arquivo = models.FileField(upload_to='atividades/entregas/', blank=True, null=True, verbose_name="Arquivo Enviado")
    texto_resposta = models.TextField(blank=True, null=True, verbose_name="Resposta em Texto")
    data_envio = models.DateTimeField(auto_now_add=True, verbose_name="Data de Envio")
    status = models.CharField(max_length=20, choices=STATUS_ENTREGA, default='pendente')
    nota_atribuida = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Nota Obtida")
    feedback_professor = models.TextField(blank=True, null=True, verbose_name="Feedback do Professor")

    class Meta:
        unique_together = ('atividade', 'aluno')

    def __str__(self):
        return f"Envio de {self.aluno} - {self.atividade.titulo}"


class Aula(models.Model):
    """Registro de cada aula ministrada para servir de base à lista de presença"""
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='aulas')
    data = models.DateField(verbose_name="Data da Aula")
    conteudo_ministrado = models.TextField(verbose_name="Conteúdo Ministrado")

    def __str__(self):
        return f"Aula de {self.data} - {self.turma.nome}"


class Presenca(models.Model):
    """Controle individual de frequência de cada aluno por aula"""
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name='presencas')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='presencas')
    presente = models.BooleanField(default=True, verbose_name="Presença")

    class Meta:
        unique_together = ('aula', 'aluno')

    def __str__(self):
        estado = "Presente" if self.presente else "Falta"
        return f"{self.aluno} - {estado} na aula de {self.aula.data}"


class Avaliacao(models.Model):
    """Instrumentos formais de avaliação (Ex: Prova Escrita, Projeto Prático)"""
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='avaliacoes')
    nome = models.CharField(max_length=100, verbose_name="Nome da Avaliação")
    peso = models.DecimalField(max_digits=4, decimal_places=2, default=1.0, help_text="Peso na média final")
    nota_maxima = models.DecimalField(max_digits=5, decimal_places=2, default=10.0)

    def __str__(self):
        return f"{self.nome} ({self.turma.nome})"


class Nota(models.Model):
    """Notas obtidas pelos alunos em cada avaliação formal"""
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='notas')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='notas')
    valor_nota = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Nota")

    class Meta:
        unique_together = ('avaliacao', 'aluno')

    def __str__(self):
        return f"{self.aluno} - Nota: {self.valor_nota} em {self.avaliacao.nome}"