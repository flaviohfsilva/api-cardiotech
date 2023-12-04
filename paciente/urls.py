from django.urls import path

from paciente.views import cadastrar_paciente, listar_pacientes, listar_pacientes_por_id
# from .views import 

urlpatterns = [
    path('cadastrarPaciente/', cadastrar_paciente, name='Pacientes'),
    path('listarPaciente/', listar_pacientes, name='Pacientes'),
    path('listarPaciente/<int:id>', listar_pacientes_por_id, name='Pacientes')
]