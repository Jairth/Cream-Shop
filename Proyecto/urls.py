from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('layout/', views.layout, name='layout'),
    path('index/', views.index, name='index'),
    path('carta/', views.carta, name='carta'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('pedidos/', views.pedidos, name="pedidos"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
