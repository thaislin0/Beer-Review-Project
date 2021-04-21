from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('review', views.review, name='review'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('cerveja', views.cerveja, name='cerveja'),
    path('', include('home.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
