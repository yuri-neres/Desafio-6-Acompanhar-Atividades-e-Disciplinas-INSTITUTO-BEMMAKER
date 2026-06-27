from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome