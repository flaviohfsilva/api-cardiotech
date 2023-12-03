from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from paciente.models import Paciente
from .serializers import PacienteSerializer

# Create your views here.
@api_view(['POST'])
def cadastrar_paciente(request):
    if request.method == 'POST':
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    serializer = PacienteSerializer(pacientes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_pacientes_por_id(request):
    id = request.query_params['id']
    pacientes = Paciente.objects.get(idPaciente=id)
    serializer = PacienteSerializer(pacientes, many=True)
    return Response(serializer.data)

