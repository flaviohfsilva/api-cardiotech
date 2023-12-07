from django.urls import path

from medicos.views import cadastrar_medico, listar_medicos, listar_medicos_por_id, excluir_medico, atualizar_informacoes, informacoes_medicos, login
# from .views import 

urlpatterns = [
    path('cadastrarMedico/', cadastrar_medico),
    path('listarMedico/', listar_medicos),
    path('listarMedico/<int:id>', listar_medicos_por_id),
    path('excluirMedico/<int:id>', excluir_medico),
    path('atualizarInformacoes/<int:id>', atualizar_informacoes),
    path('informacaoMedico/<int:id>', informacoes_medicos),
    path('login/', login)
]