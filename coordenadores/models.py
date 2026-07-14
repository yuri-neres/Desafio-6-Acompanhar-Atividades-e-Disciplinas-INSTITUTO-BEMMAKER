from django.db import models
from django.contrib.auth.models import User

class Coordenador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_coordenador', null=True, blank=True)
    
    registro_coordenacao = models.CharField(max_length=20, unique=True, verbose_name="Registro de Coordenação", null=True, blank=True)
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")

    def __str__(self):
        return f"Coordenador(a) {self.usuario.get_full_name()}"