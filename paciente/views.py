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
    paciente = Paciente.objects.all()
    serializer = PacienteSerializer(paciente, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_paciente_por_id(request, id):
    paciente = Paciente.objects.filter(idPaciente=id).first()
    serializer = PacienteSerializer(paciente)
    return Response(serializer.data)


@api_view(['GET'])
def listar_total_pacientes(request):
    pacientes = Paciente.objects.all()
    serializer = PacienteSerializer(pacientes, many=True)
    total = pacientes.count()
    data = {'Total de pacientes': total}
    return Response(data, content_type='application/json')

