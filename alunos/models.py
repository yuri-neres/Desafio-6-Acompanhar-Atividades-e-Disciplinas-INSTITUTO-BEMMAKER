from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_aluno', null=True, blank=True)
    
    matricula = models.CharField(max_length=20, unique=True, verbose_name="Matrícula", null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF", null=True, blank=True)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento", null=True, blank=True)
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")

    def __str__(self):
        return f"{self.usuario.get_full_name()} ({self.matricula})"