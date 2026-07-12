from django.db import models
from professores.models import Professor

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    
    
    professor = models.ForeignKey(
        Professor, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="Professor Responsável"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"