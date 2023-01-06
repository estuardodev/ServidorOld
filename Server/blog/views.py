from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404 # Respuesta HTTP
from django.views import generic
from django.db.models import Q

from .models import Articulo, IPUsuarios
from portafolio.views import get_user_public_ip

# Create your views here.
def indexView(request):
    # Captura de IP y guardada en BD
    ip = get_user_public_ip(request)
    user_agent = request.headers['User-Agent']
    try:
        client = IPUsuarios.objects.get(ip=ip) 
        client.navigator = user_agent
        client.visits += 1
        client.save()
    except(IPUsuarios.DoesNotExist):
        new_client = IPUsuarios.objects.create(
            ip=ip,
            navigator=user_agent,
            visits=1
        )
        new_client.save()

    articulos = Articulo.objects.all().order_by('-id')
    articulos2 = Articulo.objects.all().count()
    img = Articulo.objects.filter(id=1)
    resta = articulos2 - 6
    search = request.GET.get('search')
    if search:
        articulo1 = Articulo.objects.filter(
        Q(titulo__icontains=search) |
        Q(tags__icontains=search) |
        Q(creado__icontains=search) 
        ).distinct()
        articulo = {'search': articulo1 }
        return render(request, 'blog/index.html', articulo)
    all = request.POST.get('all')
    if all:
        all = Articulo.objects.all().order_by('-id')
        articulo = {'search': articulo1 }
        return render(request, 'blog/index.html', articulo)
    return render(request, 'blog/index.html', {'articulos': articulos, 'resta': resta, 'img':img,})

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
        return render(request, 'blog/error_blog/404/404.html')

def allView(request):
    articulos = Articulo.objects.all().order_by('-id')
    no = 1
    return render(request, 'blog/all.html', {'all': articulos, 'no': no})

# SEO
class RobotsView(generic.TemplateView):
    template_name="blog/robots.txt"
    content_type="text/plain"

class SitemapView(generic.TemplateView):
    template_name="blog/sitemap.xml"
    content_type="text/xml"
    
def RssView(request):
    template_name="rss.xml"
    data = Articulo.objects.all()
    
    return render(request, template_name, {'data':data}, content_type="text/xml")

# ERRORES
def Error404(request, exception=None):
    template_name: str = "blog/error_blog/404/404.html"
    return render(request, template_name)

def Error500(request):
    template_name: str = "blog/error_blog/500/500.html"
    return render(request, template_name, status=500)