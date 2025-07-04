from django.urls import path

from . import views

urlpatterns = [
    path('movimentacoes/', views.movimentacoes_estoque, name='movimentacoes_estoque'),
    path('movimentacoes/nova/', views.nova_movimentacao, name='nova_movimentacao'),   
    path('relatorio/estoque-baixo/', views.relatorio_estoque_baixo, name='relatorio_estoque_baixo'),
    path('vendas/nova/', views.nova_venda, name='nova_venda'),
]   