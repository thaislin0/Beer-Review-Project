from django.urls import path, include
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('<int:cervejas_id>/', views.cervejas, name='cervejas'),
    path('buscar', views.buscar, name='buscar'),
    path('usuarios/', include('usuarios.urls')),
]
