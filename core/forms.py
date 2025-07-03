from django import forms 

from .models import MovimentacaoEstoque

class MovimentacaoEstoqueForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ['produto','tipo', 'quantidade', 'observacao']
