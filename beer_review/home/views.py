from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Cervejas
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    return render(request, 'home.html')


def catalogo(request):
    cervejas = Cervejas.objects.order_by('-date_public').filter(publicada=True)
    paginator = Paginator(cervejas, 4)
    page = request.GET.get('page')
    cervejas_pagina = paginator.get_page(page)
    return render(request, 'catalogo.html', {'cervejas': cervejas_pagina})


def cervejas(request, cervejas_id):
    cervejas = get_object_or_404(Cervejas, pk=cervejas_id)
    return render(request, 'cervejas.html', {'cervejas': cervejas})


def buscar(request):
    lista_cervejas = Cervejas.objects.order_by('-date_public').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_cervejas = lista_cervejas.filter(nome_cerveja__contains=nome_a_buscar)

    return render(request, 'buscar.html', {'cervejas': lista_cervejas})
