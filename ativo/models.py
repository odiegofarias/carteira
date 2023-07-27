from django.db import models


class Corretora(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome


OPERACAO_CHOICES = (
    ('R', 'Retirada'),
    ('A', 'Aporte')
)


class Ativo(models.Model):
    ativo = models.CharField(max_length=6)
    corretora = models.ForeignKey(Corretora, on_delete=models.DO_NOTHING, related_name="corretora")
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    data_compra = models.DateField()
    taxa = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    cotacao_atual = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    tipo_de_operacao = models.CharField(max_length=1, choices=OPERACAO_CHOICES)
    quantidade = models.IntegerField()

    def __str__(self) -> str:
        return self.ativo
    
    
