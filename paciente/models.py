from django.db import models

# Create your models here.
class Paciente(models.Model):
    idPaciente = models.AutoField(primary_key=True)
    nomeCompleto = models.CharField(max_length=255)
    dataNascimento = models.DateField()
    sexo = models.CharField(max_length=10)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    orgaoEmissor = models.CharField(max_length=100)
    UF = models.CharField(max_length=2)
    estadoCivil = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    endereço = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='fotos/pacientes')



class Meta:
    ordering = ['idPaciente', 'nomeCompleto']
    verbose_name = 'Paciente'
    verbose_name_plural = 'Pacientes'
