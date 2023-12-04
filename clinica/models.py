from django.db import models

from medicos.models import Medico


# Create your models here.
class Clinica(models.Model):
    idClinica = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=255)
    razaoSocial = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)


class Meta:
    ordering = ['idClinica', 'nome_clinica']
    verbose_name = 'Clinica'
    verbose_name_plural = 'Clinicas'