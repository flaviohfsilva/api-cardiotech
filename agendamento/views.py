from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import status

from agendamento.models import Agendamento
from .serializer import AgendamentoSerializer

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
    medicos = Agendamento.objects.all()
    serializer = AgendamentoSerializer(medicos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_agendamentos_por_id(request):
    id = request.query_params['id']
    agenda = Agendamento.objects.get(idMedico=id)
    serializer = AgendamentoSerializer(agenda, many=True)
    return Response(serializer.data)

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