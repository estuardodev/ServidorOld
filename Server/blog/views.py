from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404 # Respuesta HTTP
from django.views import generic
from django.db.models import Q

from .models import Articulo, IPUsuarios
from portafolio.views import get_user_public_ip


# Capturar, Guardar Data
def UsuariosCap(request):
    # Captura de IP y guardada en BD
    ip = get_user_public_ip(request)
    user_agent = request.headers['User-Agent']
    response = HttpResponse()
    status = response.status_code
    try:
        client = IPUsuarios.objects.get(ip=ip) 
        client.navigator = user_agent
        client.visits += 1
        client.code_status = int(status)
        client.save()
    except(IPUsuarios.DoesNotExist):
        new_client = IPUsuarios.objects.create(
            ip=ip,
            navigator=user_agent,
            visits=1
        )
        new_client.save()

# Create your views here.
def indexView(request):
    # Captura de datos
    UsuariosCap(request)

    # Optencion de Articulos
    articulos = Articulo.objects.all().order_by('-id') # Se obtienen y se ordenan del ultimo al primero
    articulos2 = Articulo.objects.all().count() # Se cuentan cuantos articulos hay
    img = Articulo.objects.filter(id=1) # Imagen de la pestaña
    resta = articulos2 - 6 # Resta para articulos a mostrar

    # Se obtiene el search del sitio
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
    # Se obtiene el Mostrar todos
    if all:
        all = Articulo.objects.all().order_by('-id')
        articulo = {'search': articulo1 }
        return render(request, 'blog/index.html', articulo)
    
    # Se renderiza sin importar algo
    return render(request, 'blog/index.html', {'articulos': articulos, 'resta': resta, 'img':img,})

def ArticuloView(request, url:str, id:int):
    # Captura de datos
    UsuariosCap(request)

    # Guarda Visita
    visita = Articulo.objects.get(id=id)
    visita.visits += 1
    visita.save()

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
    # Captura de datos
    UsuariosCap(request)

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
    # Captura de datos
    UsuariosCap(request)
    
    template_name: str = "blog/error_blog/404/404.html"
    return render(request, template_name)

def Error500(request):
    template_name: str = "blog/error_blog/500/500.html"
    return render(request, template_name, status=500)