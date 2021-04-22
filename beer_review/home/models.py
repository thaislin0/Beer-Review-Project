from django.db import models
from pessoas.models import Pessoa


class Cervejas(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    Origem = models.CharField(max_length=150)
    Alcool = models.IntegerField()
    Familia = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    Tipo = models.CharField(max_length=150, default="", editable=True)
    image = models.ImageField(blank=True, upload_to='home/images')
    nota = models.IntegerField(default=5)

    def __str__(self):
        return self.title
