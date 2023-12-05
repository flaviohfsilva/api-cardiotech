from django.urls import path

from paciente.views import cadastrar_paciente, listar_pacientes, listar_paciente_por_id, listar_total_pacientes
# from .views import 

urlpatterns = [
    path('cadastrarPaciente/', cadastrar_paciente, name='Pacientes'),
    path('listarPaciente/', listar_pacientes, name='Pacientes'),
    path('listarPaciente/<int:id>', listar_paciente_por_id, name='Pacientes'),
    path('totalPacientes/', listar_total_pacientes, name='Pacientes')
]