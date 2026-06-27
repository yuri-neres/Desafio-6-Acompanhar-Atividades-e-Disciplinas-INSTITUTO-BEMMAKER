from django.db import models

class Coordenador(models.Model):
    SETOR_CHOICES = [
        ('FUNDAMENTAL', 'Ensino Fundamental'),
        ('MEDIO', 'Ensino Médio'),
        ('TECNICO', 'Ensino Técnico'),
    ]

    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=20, choices=SETOR_CHOICES, default='FUNDAMENTAL')
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome