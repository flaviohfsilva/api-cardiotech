from django.urls import path
from .views import criar_clinica

urlpatterns = [
    path('Clinica/', criar_clinica, name='Clínica')
]