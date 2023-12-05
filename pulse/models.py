from django.db import models
from medicos.models import Medico
from clinica.models import Clinica
from paciente.models import Paciente

# Create your models here.
class Pulse(models.Model):
    idAnalise = models.AutoField(primary_key=True)
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    slp = models.IntegerField()
    thall = models.IntegerField()
    caa = models.IntegerField()
    exang = models.IntegerField()
    chol = models.IntegerField()
    trtbps = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    oldpeak = models.FloatField()
    output = models.IntegerField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class Meta:
    ordering = ['idAnalise']
    verbose_name = 'Pulse'
    verbose_name_plural = 'Pulse'


def __str__(self):
    return f"{'age: ', self.age}-{'sex: ', self.sex}-{'cp: ', self.cp}-{'slp: ', self.slp}-{'thall: ', self.thall}-{'caa: ', self.caa}-{'exang: ', self.exang}-{'chol: ', self.chol}-{'trtbps: ', self.trtbps}-{'fbs: ', self.fbs}-{'restecg: ', self.restecg}-{'thalach: ', self.thalach}-{'oldpeak: ',self.oldpeak}-{'output: ', self.output}"
