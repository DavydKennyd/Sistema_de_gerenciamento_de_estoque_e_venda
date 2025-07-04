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
    VendaItemFormSet = modelformset_factory(VendaItem, form=VendaItemForm, extra=1, can_delete=True)

    if request.method == 'POST':
        venda_form = VendaForm(request.POST)
        formset = VendaItemFormSet(request.POST, queryset=VendaItem.objects.none())

        if venda_form.is_valid() and formset.is_valid():
            with transaction.atomic():
                venda = venda_form.save()

                total = 0
                for form in formset:
                    if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                        item = form.save(commit=False)
                        item.venda = venda
                        item.preco_unitario = item.produto.preco
                        item.save()

                        # Atualiza o estoque
                        item.produto.quantidade_estoque -= item.quantidade
                        item.produto.save()

                        total += item.quantidade * item.preco_unitario

                venda.valor_total = total
                venda.save()

            return redirect('movimentacoes_estoque')
    else:
        venda_form = VendaForm()
        formset = VendaItemFormSet(queryset=VendaItem.objects.none())

    return render(request, 'core/nova_venda.html', {
        'venda_form': venda_form,
        'formset': formset,
    })