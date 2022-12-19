from django.shortcuts import render
from django.http import HttpResponse # Respuesta HTTP
from django.views import generic

from .models import Articulo

# Create your views here.
def indexView(request):
    articulos = Articulo.objects.all().order_by('-id')
    articulos2 = Articulo.objects.all().count()
    img = Articulo.objects.filter(id=1)
    
    resta = articulos2 - 6
    return render(request, 'blog/index.html', {'articulos': articulos, 'resta': resta, 'img':img})

def BienvenidaView(request):
    articulo = Articulo.objects.filter(id=1)
    return render(request, 'blog/articulo/bienvenida.html', {'articulo': articulo})

def ChatGPT3View(request):
    articulo = Articulo.objects.filter(id=2)
    return render(request, 'blog/articulo/ChatGPT3View.html', {'articulo': articulo})

def InflacionRecesion2022(request):
    articulo = Articulo.objects.filter(id=3)
    return render(request, 'blog/articulo/InflaRece2022.html', {'articulo': articulo})
    
def InflacionRecesion2022(request):
    articulo = Articulo.objects.filter(id=4)
    return render(request, 'blog/articulo/vacunaCancer.html', {'articulo': articulo})

# SEO
class RobotsView(generic.TemplateView):
    template_name="blog/robots.txt"
    content_type="text/plain"

class SitemapView(generic.TemplateView):
    template_name="blog/sitemap.xml"
    content_type="text/xml"


# ERRORES
class Error404(generic.TemplateView):
    template_name: str = "error/404/404.html"

class Error500(generic.TemplateView):
    template_name: str = "error/500/500.html"