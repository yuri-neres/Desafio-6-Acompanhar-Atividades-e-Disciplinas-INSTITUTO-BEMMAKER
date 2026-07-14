from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_professor', null=True, blank=True)
    
    registro_docente = models.CharField(max_length=20, unique=True, verbose_name="Registro Docente", null=True, blank=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True, verbose_name="Especialidade")
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")

    def __str__(self):
        return f"Prof. {self.usuario.get_full_name()}"