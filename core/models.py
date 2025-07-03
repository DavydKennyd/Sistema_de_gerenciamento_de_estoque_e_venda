from django.db import models


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    endereco = models.TextField()


    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField()
    cpf_cnpj = models.CharField(max_length=20)
    endereco = models.TextField()


    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    data_cadastro = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.nome

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Venda #{self.id} - {self.cliente.nome}'

class VendaItem(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.produto.nome} (x{self.quantidade})'
    
class MovimentacaoEstoque(models.Model):
    TIPO_CHOICES = (
        ('Entrada', 'entrada'),
        ('Saida', 'Saída'),
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)


    def __str__(self):
        return f'{self.tipo.capitalize()} de {self.quantidade} {self.produto.nome}'