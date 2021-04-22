from django.contrib import admin
from .models import Cervejas


class ListandoCervejas(admin.ModelAdmin):
    list_display = ('id', 'title', 'Origem', 'Tipo', 'Alcool', 'Familia')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title', 'Origem', 'Tipo', 'Alcool', 'Familia')
    list_filter = ('id', 'title', 'Origem', 'Tipo', 'Alcool', 'Familia')
    list_per_page = 10


admin.site.register(Cervejas, ListandoCervejas)
