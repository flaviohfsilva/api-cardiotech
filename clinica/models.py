from django.db import models

from medicos.models import Medico


# Create your models here.
class Clinica(models.Model):
    idClinica = models.AutoField(primary_key=True)
    nome_clinica = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)


class Meta:
    ordering = ['idClinica', 'nome_clinica']
    verbose_name = 'Clinica'
    verbose_name_plural = 'Clinicas'