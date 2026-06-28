from django.db import models

class Aluno(models.Model):
    PERIODO_CHOICES = [
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    ]

    nome = models.CharField(max_length=100)
    serie = models.CharField(max_length=20, verbose_name="Série/Ano")
    periodo = models.CharField(max_length=1, choices=PERIODO_CHOICES, default='M', verbose_name="Período")
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

        