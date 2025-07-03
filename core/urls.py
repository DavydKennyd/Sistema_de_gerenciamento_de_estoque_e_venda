from django.urls import path

from . import views

urlpatterns = [
    path('movimentacoes/', views.movimentacoes_estoque, name='movimentacoes_estoque'),
    path('movimentacoes/nova/', views.nova_movimentacao, name='nova_movimentacao'),   
]