from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404 # Respuesta HTTP
from django.views import generic
from django.db.models import Q

from .models import Articulo

# Create your views here.
def indexView(request):
    articulos = Articulo.objects.all().order_by('-id')
    articulos2 = Articulo.objects.all().count()
    img = Articulo.objects.filter(id=1)
    resta = articulos2 - 6
    search = request.GET.get('search')
    if search:
        articulos = Articulo.objects.filter(
            Q(titulo__icontains=search) |
            Q(tags__icontains=search) |
            Q(creado__icontains=search) 
        ).distinct()
    return render(request, 'blog/index.html', {'articulos': articulos, 'resta': resta, 'img':img})

def ArticuloView(request, url:str, id:int):
    articule = get_object_or_404(Articulo, id=id)
    try: 

        search = request.GET.get('search')
        if search:
            articulo1 = Articulo.objects.filter(
            Q(titulo__icontains=search) |
            Q(tags__icontains=search) |
            Q(creado__icontains=search) 
            ).distinct()
            articulo = {'search': articulo1 }
        else:
            articulos = Articulo.objects.filter(id=id)
            articulo = {'articulo': articulos }

        return render(request, 'blog/articulo/articulo.html', articulo)
    except (KeyError, Articulo.DoesNotExist):
        return Http404  

# SEO
class RobotsView(generic.TemplateView):
    template_name="blog/robots.txt"
    content_type="text/plain"

class SitemapView(generic.TemplateView):
    template_name="blog/sitemap.xml"
    content_type="text/xml"

class RssView(generic.TemplateView):
    template_name="rss.xml"
    content_type="text/xml"
    data = Articulo.objects.all()
    content = {'data': data}

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Articulo, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['data'] = self.data
        return context
    

# ERRORES
def handler404(request, exception=None):
    template_name: str = "error_blog/404/404.html"
    return render(request, template_name)

def Error500(request):
    template_name: str = "error_blog/500/500.html"
    return render(request, template_name, status=500)