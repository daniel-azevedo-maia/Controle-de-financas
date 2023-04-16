from django.db import models


class Receita(models.Model):
    id = models.AutoField(primary_key=True)
    CATEGORIAS = (
        ('ESCOLHA', 'Escolha uma categoria'),
        ('PRS', 'Presente'),
        ('PRM', 'Prêmio'),
        ('SLR', 'Salário'),
        ('OTS', 'Outros'),
    )

    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    data = models.DateField(auto_now_add=True, blank=False)
    descricao = models.TextField()
    categoria = models.CharField(
        max_length=10, choices=CATEGORIAS, default='ESCOLHA', blank=False)
    comprovante = models.FileField(upload_to='comprovantes/', blank=False)

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"

class Despesa(models.Model):
    id = models.AutoField(primary_key=True)
    
    CATEGORIAS = (
        ('ESCOLHA', 'Escolha uma categoria'),
        ('CSA', 'Casa'),
        ('EDU', 'Educação'),
        ('ETR', 'Eletrônicos'),
        ('LZR', 'Lazer'),
        ('SD', 'Saúde'),
        ('SPR', 'Supermercado'),
        ('TRS', 'Transporte'),
        ('OTR', 'Outros')
    )

    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    data = models.DateField(auto_now_add=True, blank=False)
    descricao = models.TextField()
    categoria = models.CharField(
        max_length=10, choices=CATEGORIAS, default='ESCOLHA', blank=False)
    comprovante = models.FileField(upload_to='comprovantes/', blank=False)

    class Meta:
        ordering = ['-data']
        verbose_name = "Despesa"
        verbose_name_plural = "Despesas"


