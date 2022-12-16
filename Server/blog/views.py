from django.shortcuts import render
from django.http import HttpResponse # Respuesta HTTP
from django.views import generic

from .models import Articulo

# Create your views here.
def indexView(request):
    articulos = Articulo.objects.all().order_by('-id')
    articulos2 = Articulo.objects.all().count()
    
    resta = articulos2 - 6
    return render(request, 'blog/index.html', {'articulos': articulos, 'resta': resta})

def BienvenidaView(request):
    articulo = Articulo.objects.filter(id=1)
    print(articulo)
    return render(request, 'blog/articulo/bienvenida.html', {'articulo': articulo})


class Error404(generic.TemplateView):
    template_name: str = "error/404/404.html"

class Error500(generic.TemplateView):
    template_name: str = "error/500/500.html"