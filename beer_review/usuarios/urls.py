from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('review', views.review, name='review'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('deleta/<int:cervejas_id>', views.deleta_cerveja, name='deleta_cerveja'),
    path('edita/<int:cervejas_id>', views.edita_cerveja, name='edita_cerveja'),
    path('atualiza', views.atualiza, name='atualiza'),
]
