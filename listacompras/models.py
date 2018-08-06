from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=80)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome_produto #Faz com que apareça o nome do produto, em vez de object.1, por exemplo.

