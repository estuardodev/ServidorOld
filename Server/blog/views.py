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

class ChatGPT3View(generic.TemplateView):
    template_name="blog/articulo/ChatGPT3View.html"
    articulo = Articulo.objects.filter(id=2)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articulo'] = self.articulo
        return context

# SEO
class RobotsView(generic.TemplateView):
    template_name="blog/robots.txt"
    content_type="text/plain"

class SitemapView(generic.TemplateView):
    template_name="blog/sitemap.xml"
    content_type="text/xml"
    data = Articulo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articulos'] = self.data
        return context

# ERRORES
class Error404(generic.TemplateView):
    template_name: str = "error/404/404.html"

class Error500(generic.TemplateView):
    template_name: str = "error/500/500.html"