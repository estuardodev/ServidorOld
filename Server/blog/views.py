from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404 # Respuesta HTTP
from django.views import generic

from .models import Articulo

# Create your views here.
def indexView(request):
    articulos = Articulo.objects.all().order_by('-id')
    articulos2 = Articulo.objects.all().count()
    img = Articulo.objects.filter(id=1)
    resta = articulos2 - 6
    return render(request, 'blog/index.html', {'articulos': articulos, 'resta': resta, 'img':img})

def ArticuloView(request, url:str, id:int):
    articule = get_object_or_404(Articulo, id=id)
    try: 
        articulo = Articulo.objects.filter(id=id)
        return render(request, 'blog/articulo/articulo.html', {'articulo': articulo})
    except (KeyError, Articulo.DoesNotExist):
        return Http404  

# SEO
class RobotsView(generic.TemplateView):
    template_name="blog/robots.txt"
    content_type="text/plain"

class SitemapView(generic.TemplateView):
    template_name="blog/sitemap.xml"
    content_type="text/xml"


# ERRORES
def Error404(request):
    template_name: str = "error_blog/404/404.html"
    return render(request, template_name, status=404)

def Error500(request):
    template_name: str = "error_blog/500/500.html"
    return render(request, template_name, status=500)