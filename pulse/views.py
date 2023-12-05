# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# # from joblib import load
# from sklearn.metrics.pairwise import euclidean_distances
# import joblib

# from pulse.serializer import PulseSerializer


# # Create your views here.

# PULSE_MODEL = joblib.load('pulse_model_knn.pkl')

# @api_view(['POST'])
# def pulse_analise(request):

#     if request == 'POST':
#         serializer = PulseSerializer(data=request.data)

#         if serializer.is_valid():
#             dados_pulse = serializer.validated_data
#             predict = PULSE_MODEL.predict(dados_pulse)
#             serializer.save(predict)
#             return Response({"Resultado": predict }, status=status.HTTP_201_CREATED)
    




    




