from django.db import models
from django.contrib.auth.models import User


class Equipamento(models.Model):
    EQUIP_CHOICES = (
        ('C','Cadastro'),
        ('S', 'Saida Manutenção'),
        ('E', 'Retorno Conserto'),
        ('D', 'Descarte ou Sem Conserto')
    )
    tipo = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    movimentacao = models.CharField(max_length=1, choices=EQUIP_CHOICES, blank=False, null=False)
    data_movimentacao = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo
    