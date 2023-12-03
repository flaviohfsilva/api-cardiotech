from django.urls import path

from medicos.views import cadastrar_medico, listar_medicos, listar_medicos_por_id, excluir_medico
# from .views import 

urlpatterns = [
    path('cadastrarMedico/', cadastrar_medico),
    path('listarMedico/', listar_medicos),
    path('listarMedico/<int:id>', listar_medicos_por_id),
    path('excluirMedico/<int:id>', excluir_medico)
]