from django.db import models
from disciplinas.models import Disciplina

class Atividade(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título da Atividade")
    descricao = models.TextField(verbose_name="Descrição")
    data_entrega = models.DateField(verbose_name="Data de Entrega")
    disciplina = models.ForeignKey(
        Disciplina, 
        on_delete=models.CASCADE, 
        verbose_name="Disciplina"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Atividade Acadêmica"
        verbose_name_plural = "Atividades Acadêmicas"