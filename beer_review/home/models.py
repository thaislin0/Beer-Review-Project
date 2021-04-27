from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Cervejas(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_cerveja = models.CharField(max_length=150)
    origem_cerveja = models.CharField(max_length=150)
    quantidade_alcool = models.IntegerField()
    familia_cerveja = models.CharField(max_length=150)
    descricao_cerveja = models.CharField(max_length=150)
    tipo_cerveja = models.CharField(max_length=150, default="", editable=True)
    foto_cerveja = models.ImageField(upload_to='home/images')
    nota_cerveja = models.IntegerField(default=5)
    publicada = models.BooleanField(default=False)
    date_public = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome_cerveja
