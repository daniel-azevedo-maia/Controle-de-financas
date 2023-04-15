from django.db import models

class Receita(models.Model):
    CATEGORIAS = (
        ('ESCOLHA', 'Escolha uma categoria'),
        ('SLR', 'Salario'),
        ('MSD', 'Mesada'),
        ('VDA', 'Vendas avulsa')
    )

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)
    descricao = models.TextField()
    categoria = models.CharField(
        max_length=10, choices=CATEGORIAS, default='ESCOLHA')
    comprovante = models.FileField()

    class Meta:
        verbose_name = "Receita"
        verbose_name_plurar = "Receitas"

class Despesa(models.Model):
    CATEGORIAS = (
        ('ESCOLHA', 'Escolha uma categoria'),
        ('AL', 'Alimentação'),
        ('MRD', 'Moradia'),
        ('TSP', 'Transporte'),
        ('SD', 'Saúde'),
        ('LZR', 'Lazer'),
        ('TEL', 'Telefone'),
        ('INT', 'Internet'),
        ('EDU', 'Educação')
    )

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)
    descricao = models.TextField()
    categoria = models.CharField(
        max_length=10, choices=CATEGORIAS, default='ESCOLHA')
    comprovante = models.FileField()

    class Meta:
        ordering = ['-data']
        verbose_name = "Despesa"
        verbose_name_plurar = "Despesas"


