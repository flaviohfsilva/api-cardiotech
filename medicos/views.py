import random
import string
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth import authenticate
# from rest_framework.authentication import TokenAuthentication
# from rest_framework_jwt.authentication import api_settings


from medicos.models import Medico
from .serializers import MedicoSerializer

# Create your views here.

# @api_view(['POST'])
# def login(request):
#     data = request.data
#     try:
#         medico = authenticate(crm=data['crm'], senha=data['senha'])
#     except KeyError:
#         return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

#     if medico is not None:
#         jwt_payload = {
#             'idMedico': medico.id,
#             'nome': medico.nomeCompleto,
#             'crm': medico.crm
#         }
#         token = api_settings.JWT_PAYLOAD_HANDLER(jwt_payload)
#         return Response({'Token': token, 'Médico': jwt_payload})

#     return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@parser_classes([JSONParser])
def cadastrar_medico(self, request):
    if request.method == 'POST':
        serializer = MedicoSerializer(data=request.data)
        if serializer.is_valid():
            senha = generate_password()
            medico = serializer.save(senha=senha)
            return Response(serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def listar_medicos(request):
    medicos = Medico.objects.all()
    serializer = MedicoSerializer(medicos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_medicos_por_id(request, id):
    medicos = Medico.objects.filter(idMedico=id)
    serializer = MedicoSerializer(medicos, many=True)
    # print('Médico pesquisado:', serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def informacoes_medicos(request, id):
    medicos = Medico.objects.filter(idMedico=id).first()
    # medico = medicos.first()
    serializer = MedicoSerializer(medicos)
    nome = serializer.data.get('nomeCompleto')
    return Response({'Nome': nome})

# @api_view(['POST'])
# def login():

# @api_view(['PATCH'])
# def atualizar_senha():

@api_view(['PUT'])
def atualizar_informacoes(request, id):
    medico = Medico.objects.get(idMedico=id)

    serializer = MedicoSerializer(medico, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK, content_type='application/json')

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def excluir_medico(request, id):
    medico = Medico.objects.get(idMedico=id)
    try:
        medico.delete()
        return Response(data={'mensagem': mensagens['cancelamento']['sucesso']}, status=status.HTTP_200_OK)
    except Medico.DoesNotExist:
        return Response(data={'error': mensagens['cancelamento']['erro']}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(data={'error': mensagens['cancelamento']['erro'].format(e)}, status=status.HTTP_400_BAD_REQUEST)
    


def generate_password():
    # Gera uma senha aleatória
    senha = ''.join(
        random.choice(string.ascii_lowercase + string.digits)
        for _ in range(12)
    )

    # Criptografa a senha
    senha_cifrada = make_password(senha)

    return senha_cifrada

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