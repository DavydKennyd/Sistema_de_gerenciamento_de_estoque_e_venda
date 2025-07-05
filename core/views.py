from django.shortcuts import render, redirect
from .models import MovimentacaoEstoque, Produto,models,Venda, VendaItem, Cliente
from .forms import MovimentacaoEstoqueForm,VendaForm, VendaItemForm
from django.forms import modelformset_factory
from django.db import transaction

def movimentacoes_estoque(request):
    movimentacoes = MovimentacaoEstoque.objects.all().order_by('-data')
    return render(request, 'core/movimentacoes.html', {'movimentacoes': movimentacoes})


def nova_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoEstoqueForm(request.POST)
        if form.is_valid():
            movimentacao = form.save()

            produto = movimentacao.produto
            if movimentacao.tipo == 'entrada':
                produto.quantidade_estoque += movimentacao.quantidade
            elif movimentacao.tipo == 'saida':
                produto.quantidade_estoque -= movimentacao.quantidade
            produto.save()

            return redirect('movimentacoes_estoque')
    else:
        form = MovimentacaoEstoqueForm()

    return render(request, 'core/nova_movimentacao.html', {'form': form})



def relatorio_estoque_baixo(request):
    produto_baixo_estoque = Produto.objects.filter(quantidade_estoque__lt=models.F('estoque_minimo'))
    return render(request, 'core/relatorio_estoque_baixo.html', {'produtos': produto_baixo_estoque})


def nova_venda(request):
    if request.method == 'POST':
        venda_form = VendaForm(request.POST)
        item_form = VendaItemForm(request.POST)

        if venda_form.is_valid() and item_form.is_valid():
            venda = venda_form.save()

            item = item_form.save(commit=False)
            item.venda = venda
            item.preco_unitario = item.produto.preco
            item.save()

            # atualizar estoque
            item.produto.quantidade_estoque -= item.quantidade
            item.produto.save()

            return redirect('movimentacoes_estoque')
    else:
        venda_form = VendaForm()
        item_form = VendaItemForm()

    return render(request, 'core/nova_venda.html', {
        'venda_form': venda_form,
        'item_form': item_form,
    })