from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('layout/', views.layout, name='layout'),
    path('index/', views.index, name='index'),
    path('carta/', views.carta, name='carta'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('pedidos/', views.pedidos, name="pedidos"),
]
