from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('carta/', views.carta),
    path('contacto/', views.contacto),
    path('nosotros/', views.nosotros),
    path('pedidos/', views.pedidos)
]
