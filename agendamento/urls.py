from django.urls import path

from agendamento.views import agendar_consulta, listar_agendamento, listar_agendamentos_por_id, cancelar_consulta
# from .views import 

urlpatterns = [
    path('agendarConsulta/', agendar_consulta),
    path('listarAgendamento/', listar_agendamento),
    path('listarAgendamento/<int:id>', listar_agendamentos_por_id),
    path('cancelarConsulta/<int:id>', cancelar_consulta)
]