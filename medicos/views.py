from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from medicos.models import Medico
from .serializers import MedicoSerializer

# Create your views here.
@api_view(['POST'])
def cadastrar_medico(request):
    if request.method == 'POST':
        serializer = MedicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_medicos(request):
    medicos = Medico.objects.all()
    serializer = MedicoSerializer(medicos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_medicos_por_id(request):
    id = request.query_params['id']
    medicos = Medico.objects.get(idMedico=id)
    serializer = MedicoSerializer(medicos, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def login():

# @api_view(['PATCH'])
# def atualizar_senha():


@api_view(['DELETE'])
def excluir_medico():
    medico = Medico.objects.get(idMedico=id)
    try:
        medico.delete()
        return Response(data={'mensagem': mensagens['cancelamento']['sucesso']}, status=status.HTTP_200_OK)
    except Medico.DoesNotExist:
        return Response(data={'error': mensagens['cancelamento']['erro']}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(data={'error': mensagens['cancelamento']['erro'].format(e)}, status=status.HTTP_400_BAD_REQUEST)
    


mensagens = {
    # 'agendamento':{
    #     'sucesso': 'Consulta agendada com sucesso!',
    #     'erro': 'Erro ao agendar consulta: {}'
    # },

    'cancelamento': {
        'sucesso': 'Médico excluído com sucesso!',
        'erro': 'Erro ao excluir médico: {}'
    }
}