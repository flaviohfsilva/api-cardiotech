from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from clinica.models import Clinica
from .serializers import ClinicaSerializer

# Create your views here.

@api_view(['POST'])
# @parser_classes([JSONParser])
def criar_clinica(request):
    print(f'Received data: {request.data}')
    if request.method == 'POST':
        serializer = ClinicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listar_clinica(request):
    clinicas = Clinica.objects.all()
    serializer = ClinicaSerializer(clinicas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_clinica_por_id(request):
    id = request.query_params['id']
    clinica = Clinica.objects.get(idClinica=id)
    serializer = ClinicaSerializer(clinica)
    return Response(serializer.data)
