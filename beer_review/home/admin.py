from django.contrib import admin
from .models import Cervejas
from pessoas.models import Pessoa


class ListandoCervejas(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'nome_cerveja', 'origem_cerveja', 'tipo_cerveja', 'quantidade_alcool', 'familia_cerveja', 'publicada')
    list_display_links = ('id', 'nome_cerveja',)
    search_fields = ('id', 'nome_cerveja', 'origem_cerveja', 'tipo_cerveja', 'quantidade_alcool', 'familia_cerveja')
    list_filter = ('id', 'nome_cerveja', 'origem_cerveja', 'tipo_cerveja', 'quantidade_alcool', 'familia_cerveja')
    list_editable = ('publicada',)
    list_per_page = 10


admin.site.register(Cervejas, ListandoCervejas)
