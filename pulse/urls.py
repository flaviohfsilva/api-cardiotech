from django.urls import path

from pulse.views import pulse_analise, download_model
# from .views import 

urlpatterns = [
    path('analise/', pulse_analise, name='Pulse'),
    path('baixar-pulse/', download_model, name='download_model')
]