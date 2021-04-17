from django.shortcuts import render
from .models import Cervejas


def home(request):
    return render(request, 'home.html')


def review(request):
    return render(request, 'review.html')


def catalogo(request):
    cervejas = Cervejas.objects.all()
    return render(request, 'catalogo.html', {'cervejas': cervejas})


def cerveja(request):
    cervejas = Cervejas.objects.all()
    return render(request, 'cerveja.html', {'cervejas': cervejas})
