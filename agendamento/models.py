from django.db import models
from clinica.models import Clinica

from medicos.models import Medico
from paciente.models import Paciente

# Create your models here.
class Agendamento(models.Model):
    idAgendamento = models.AutoField(primary_key=True)
    data = models.DateTimeField()
    motivo = models.CharField(max_length=255)
    faltou = models.BooleanField(default=False)
    atendido = models.BooleanField(default=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, blank=True, null=True, default=None)


class Meta:
    ordering = ['idAgendamento', 'paciente', 'data']
    verbose_name = 'Agendamento'
    verbose_name_plural = 'Agendamentos'