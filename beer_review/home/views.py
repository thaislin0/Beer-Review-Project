from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Cervejas


def home(request):
    return render(request, 'home.html')


def catalogo(request):
    cervejas = Cervejas.objects.order_by('-date_public').filter(publicada=True)
    return render(request, 'catalogo.html', {'cervejas': cervejas})


def cervejas(request, cervejas_id):
    cervejas = get_object_or_404(Cervejas, pk=cervejas_id)
    return render(request, 'cervejas.html', {'cervejas': cervejas})


def buscar(request):
    lista_cervejas = Cervejas.objects.order_by('-date_public').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            lista_cervejas = lista_cervejas.filter(title__contains=nome_a_buscar)

    return render(request, 'buscar.html', {'cervejas': lista_cervejas})
