# Imports the systen
import os, mimetypes, requests

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse # Respuesta HTTP
from django.views import generic
from django.db.models import Q
from django.forms.models import model_to_dict

from .models import Articulo, IPUsuarios
from ipware import get_client_ip
from portafolio.views import monitor_the_cpu_and_memory


# Capturar, Guardar Data
def UsuariosCap(request):
    '''With this function recolect and save the information of the users'''
    ip, v_f = get_client_ip(request)
    user_agent = request.headers['User-Agent']
    petition = requests.get(f"http://ip-api.com/json/{ip}")
    petition = petition.json()
    if petition['status'] == "success":
    
        try:
            # Save IPUsers
            cliente = IPUsuarios.objects.get(ip=ip)
            cliente.browser = user_agent
            cliente.country = petition['country']
            cliente.city = petition['city']
            cliente.lat = petition['lat']
            cliente.lon = petition['lon']
            cliente.code_zip = petition['zip']
            cliente.isp = petition['isp']
            cliente.visits += 1
            cliente.save()
            
        except (IPUsuarios.DoesNotExist):
            create = IPUsuarios.objects.create(
                ip=ip, 
                browser=user_agent, 
                country=petition['country'], 
                city = petition['city'],
                lat = petition['lat'],
                lon = petition['lon'],
                code_zip = petition['zip'],
                isp = petition['isp'],
                visits=1)            
            create.save()
        return ip, user_agent
    else:
        try:
            # Save IPUsers
            cliente = IPUsuarios.objects.get(ip=ip)
            cliente.browser = user_agent
            cliente.country = "LocalHost",
            cliente.city = "LocalHost",
            cliente.lat = "LocalHost",
            cliente.lon = "LocalHost",
            cliente.code_zip = "LocalHost",
            cliente.isp = "LocalHost",
            cliente.visits += 1
            cliente.save()
            
        except IPUsuarios.DoesNotExist:
            create = IPUsuarios.objects.create(
                ip=ip, 
                browser=user_agent, 
                country="LocalHost", 
                city = "LocalHost",
                lat = "LocalHost",
                lon = "LocalHost",
                code_zip = "LocalHost",
                isp = "LocalHost",
                visits=1)            
            create.save()
        return ip, user_agent


# Create your views here.
def indexView(request):
    # Templates
    template_name: str = "blog/index.html"
    template_name_stop: str = "portafolio/stop.html"

    # Datos externos
    UsuariosCap(request)
    cpu, memory = monitor_the_cpu_and_memory()
    cpu, memory = float(cpu), float(memory)

    # Registros de DB
    articulos = Articulo.objects.all().order_by('-id') # Se obtienen y se ordenan del ultimo al primero
    articulos2 = Articulo.objects.all().count() # Se cuentan cuantos articulos hay
    img = Articulo.objects.filter(id=1) # Imagen de la pestaña
    resta = articulos2 - 6 # Resta para articulos a mostrar
    all = request.POST.get('all')

    # Variables
    message_alert = True
    # Verificación de si el CPU esta a mas de 90%, de ser así se renderizara el template_name_stop
    if cpu > 90:
        return render(request, template_name_stop)
    
    # Verificación de si el usuario realiza una busqueda
    search = request.GET.get('search')
    if search:
        articulo1 = Articulo.objects.filter(Q(titulo__icontains=search) | Q(tags__icontains=search) | Q(creado__icontains=search)).distinct()
        # Renderización si el usuario realizó una busqueda
        if cpu >= 80:
            articulo = {'search': articulo1, 'message_alert': message_alert, 'articulos': articulos}
            all = Articulo.objects.all().order_by('-id')    
            return render(request, 'blog/index.html', articulo)
        else:
            articulo = {'search': articulo1, 'articulos': articulos }
            all = Articulo.objects.all().order_by('-id')    
            return render(request, 'blog/index.html', articulo)
    
    # Renderización del template normalmente
    if cpu >= 80:
        return render(request, template_name, { 'message_alert': message_alert, 'articulos': articulos, 'resta': resta, 'img':img,})
    else:
        # Se renderiza sin importar algo
        return render(request, template_name, {'articulos': articulos, 'resta': resta, 'img':img,})

def getArticulo(request, pk:int):
    try:
        visitas = Articulo.objects.get(id=pk)
        js = {'message': 'success', 'article': model_to_dict(visitas, exclude=['imagen', 'alt_imagen'])}
    except Articulo.DoesNotExist:
        js = {'message': 'Not Found'}

    return JsonResponse(js)

def getIPUsers(request, ip:str):
    try:
        petition = requests.get(f"http://ip-api.com/json/{ip}")
        petition = petition.json()
        js = {'message': 'success', 'information': petition}
    except Articulo.DoesNotExist:
        js = {'message': 'Not Found'}

    return JsonResponse(js)


def ArticuloView(request, url:str, id:int):
    # Templates
    template_name: str = "blog/articulo/articulo.html"
    template_name_stop: str = "portafolio/stop.html"
    
    # Datos externos
    UsuariosCap(request)
    cpu, memory = monitor_the_cpu_and_memory()
    cpu, memory = float(cpu), float(memory)

    # Variables
    message_alert = True

    # Guarda Visita
    visita = Articulo.objects.get(id=id)
    visita.visits += 1
    visita.save()

    # Verificación de si el CPU esta a mas de 90%, de ser así se renderizara el template_name_stop
    if cpu > 90:
        return render(request, template_name_stop)

    # Verificación de si existe el articulo
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
            # Renderización si el usuario realizó una busqueda
            if cpu >= 80:
                articulo = {'search': articulo1, 'message_alert': message_alert }
        else:
            articulos = Articulo.objects.filter(id=id)
            articulo = {'articulo': articulos}
            if cpu >= 80:
                articulos = Articulo.objects.filter(id=id)
                articulo = {'articulo': articulos, 'message_alert': message_alert }

        return render(request, 'blog/articulo/articulo.html', articulo)
    except (KeyError, Articulo.DoesNotExist):
        return render(request, 'blog/error_blog/404/404.html')

def allView(request):
    # Templates
    template_name: str = "blog/all.html"
    template_name_stop: str = "portafolio/stop.html"
    
    # Datos externos
    UsuariosCap(request)
    cpu, memory = monitor_the_cpu_and_memory()
    cpu, memory = float(cpu), float(memory)

    # Variables
    message_alert = True

    # Registros de DB
    articulos = Articulo.objects.all().order_by('-id')
    no = 1

    # Verificación de si el CPU esta a mas de 90%, de ser así se renderizara el template_name_stop
    if cpu > 90:
        return render(request, template_name_stop)
    if cpu >= 80:
        # Retorno en caso de estar a 80% el CPU
        return render(request, template_name, {'all': articulos, 'no': no, 'message_alert': message_alert})
    else:
        # Retorno sin sobre carga alguna
        return render(request, template_name, {'all': articulos, 'no': no})

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