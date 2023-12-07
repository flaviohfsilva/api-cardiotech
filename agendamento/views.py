from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import status

from agendamento.models import Agendamento
from .serializer import AgendamentoSerializer
from medicos.serializers import MedicoSerializer

# Create your views here.
@api_view(['POST'])
@parser_classes([JSONParser])
def agendar_consulta(request):
    if request.method == 'POST':
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 'Consulta agendada com sucesso!', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, 'Error ao agendar consulta ',status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_agendamento(request):
    agendamentos = Agendamento.objects.all()
    dados = []

    for agenda in agendamentos:
        paciente = agenda.paciente
        medico = agenda.medico
        clinica = agenda.clinica

        dados_agenda = {
            "idAgendamento": agenda.idAgendamento,
            "paciente": paciente.nomeCompleto,
            "data": agenda.data,
            "motivo": agenda.motivo,
            "medico": medico.nomeCompleto,
            "idMedico": medico.idMedico,
            "clinica": clinica.nome
        }

        dados.append(dados_agenda)

    serializer = AgendamentoSerializer(agendamentos, many=True)
    # print("oi", dados)
    return Response(dados)

@api_view(['GET'])
def listar_agendamentos_por_id(request, id):
    print(request)
    agenda = Agendamento.objects.filter(idAgendamento=id).exists()
    if not agenda:
        return Response({'error': 'Agendamento não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    agenda = Agendamento.objects.filter(idAgendamento=id).first()
    
    medico = agenda.medico
    paciente = agenda.paciente
    clinica = agenda.clinica

    dados = {
        "paciente": paciente.nomeCompleto,
        "data": agenda.data,
        "motivo": agenda.motivo,
        "medico": medico.nomeCompleto,
        "clinica": clinica.nome
    }

    # print(dados)

    return Response(dados)


@api_view(['GET'])
def listar_pacientes_atendidos(request):
    agendamentos_atendidos = Agendamento.objects.filter(atendido=True)
    dados = []

    for agenda in agendamentos_atendidos:

        paciente = agenda.paciente

        dados_agenda_atendidos = {
            "idAgendamento": agenda.idAgendamento,
            "paciente": paciente.nomeCompleto,
            "atendido": agenda.atendido
        }

        dados.append(dados_agenda_atendidos)

    serializer = AgendamentoSerializer(agendamentos_atendidos, many=True)
    # print("oi", dados)
    return Response(dados)

@api_view(['GET'])
def listar_pacientes_faltantes(request):
    pacientes_faltantes = Agendamento.objects.filter(faltou=True)
    dados = []

    for agenda in pacientes_faltantes:

        paciente = agenda.paciente

        dados_agenda_faltas = {
            "idAgendamento": agenda.idAgendamento,
            "paciente": paciente.nomeCompleto,
            "data": agenda.data,
            "motivo": agenda.motivo,
            "faltou": agenda.faltou
        }

        dados.append(dados_agenda_faltas)

    serializer = AgendamentoSerializer(pacientes_faltantes, many=True)
    # print("oi", dados)
    return Response(dados)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def cancelar_consulta(request, id):
    agenda = Agendamento.objects.get(idAgendamento=id)
    try:
        agenda.delete()
        return Response(data={'mensagem': mensagens['cancelamento']['sucesso']}, status=status.HTTP_200_OK)
    except Agendamento.DoesNotExist:
        return Response(data={'error': mensagens['cancelamento']['erro']}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(data={'error': mensagens['cancelamento']['erro'].format(e)}, status=status.HTTP_400_BAD_REQUEST)


mensagens = {
    # 'agendamento':{
    #     'sucesso': 'Consulta agendada com sucesso!',
    #     'erro': 'Erro ao agendar consulta: {}'
    # },

    'cancelamento': {
        'sucesso': 'Consulta cancelada com sucesso!',
        'erro': 'Erro ao cancelar consulta: {}'
    }
}