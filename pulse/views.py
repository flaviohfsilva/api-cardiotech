import base64
import os
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
# from joblib import load
from sklearn.metrics import euclidean_distances
import joblib

from pulse.serializer import PulseSerializer


# # Create your views here.

# Diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho diretório Pulse
caminho_arquivo = os.path.join(diretorio_atual, 'pulse_model_knn.pkl')

PULSE_MODEL = joblib.load(caminho_arquivo)

@api_view(['POST'])
def pulse_analise(request):

    if request == 'POST':
        serializer = PulseSerializer(data=request.data)

        if serializer.is_valid():
            dados_pulse = serializer.validated_data
            predict = PULSE_MODEL.predict(dados_pulse)
            serializer.save(predict)
            return Response({"Resultado": predict }, status=status.HTTP_201_CREATED)
        

@csrf_exempt
@api_view(['GET'])
def download_model(request):
    try:
        # Carregar o modelo salvo
        model = joblib.load('pulseIA_model_knn.pkl')

        # Serializar o modelo para base64
        model_base64 = base64.b64encode(joblib.dumps(model)).decode('utf-8')

        # Responder com o modelo serializado
        return Response({'model': model_base64})

    except Exception as e:
        # Tratar erros, se necessário
        return Response({'error': str(e)}, status=500)
    




    




