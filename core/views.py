from django.shortcuts import render, redirect
from .models import MovimentacaoEstoque, Produto
from .forms import MovimentacaoEstoqueForm


def movimentacoes_estoque(request):
    movimentacoes = MovimentacaoEstoque.objects.all().order_by('-data')
    return render(request, 'core/movimentacoes.html', {'movimentacoes': movimentacoes})


def nova_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoEstoqueForm(request.POST)
        if form.is_valid():
            movimentacao = form.save()

            # Atualiza o estoque
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

    