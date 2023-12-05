from django.urls import path
from .views import criar_clinica, listar_clinica, listar_clinica_por_id, clinica_medico

urlpatterns = [
    path('cadastrarClinica/', criar_clinica, name='Clínica'),
    path('listarClinica/', listar_clinica, name='Clínica'),
    path('listarClinica/<int:id>', listar_clinica_por_id, name='listar_clinica'),
    path('medico/<int:id>', clinica_medico)
]