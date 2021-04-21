from django.shortcuts import render, get_object_or_404
from .models import Cervejas


def home(request):
    return render(request, 'home.html')


def review(request):
    return render(request, 'review.html')


def catalogo(request):
    cervejas = Cervejas.objects.all()
    return render(request, 'catalogo.html', {'cervejas': cervejas})


def cervejas(request, cervejas_id):
    cervejas = get_object_or_404(Cervejas, pk=cervejas_id)
    return render(request, 'cervejas.html', {'cervejas': cervejas})
