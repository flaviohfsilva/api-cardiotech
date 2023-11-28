from django.db import models

# Create your models here.

class Medico(models.Model):
    idMedico = models.AutoField(primary_key=True)
    crm = models.CharField(max_length=6)
    senha = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    numero = models.CharField(max_length=16)
    nomeCompleto = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='fotos/medicos')

class Meta:
    ordering = ['idMedico', 'crm']
    verbose_name = 'Medico'
    verbose_name_plural = 'Medicos'
