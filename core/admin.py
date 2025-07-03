from django.contrib import admin
from .models import Fornecedor, Cliente, Produto, Venda, VendaItem, MovimentacaoEstoque

admin.site.register(Fornecedor)
admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(VendaItem)
admin.site.register(MovimentacaoEstoque)
