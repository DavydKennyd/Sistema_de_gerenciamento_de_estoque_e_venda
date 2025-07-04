from django import forms 

from .models import MovimentacaoEstoque,Venda, VendaItem

class MovimentacaoEstoqueForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ['produto','tipo', 'quantidade', 'observacao']


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente']

class VendaItemForm(forms.ModelForm):
    class Meta:
        model = VendaItem
        fields = ['produto', 'quantidade']