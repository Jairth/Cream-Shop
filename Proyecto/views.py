from django.shortcuts import render


def index(request):
  return render(request, 'index.html')

# def layout(request):
#   return render(request), 'layout.html'  

def carta(request):
  return render(request, 'carta.html')

def contacto(request):
  return render(request, 'contacto.html')

def nosotros(request):
  return render(request,'nosotros.html')

def pedidos(request):
  return render(request, 'pedidos.html')