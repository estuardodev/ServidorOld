# Imports the systen
import os, mimetypes, requests

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse # Respuesta HTTP
from django.views import generic
from django.db.models import Q


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


from django.shortcuts import render
from django.db.models import Q
from .models import Articulo

from django.shortcuts import render
from django.db.models import Q
from .models import Articulo

def indexView(request):
    template_name = "blog/index.html"
    template_name_stop = "portafolio/stop.html"
    message_alert = True

    # Verificación de si el CPU está a más del 90%, en ese caso se renderiza el template_name_stop
    cpu, memory = monitor_the_cpu_and_memory()
    cpu, memory = float(cpu), float(memory)
    if cpu > 90:
        return render(request, template_name_stop)

    # Obtener registros de DB
    articulos = Articulo.objects.filter(status=True).order_by('-id')  # Se obtienen y se ordenan del último al primero
    articulos_count = articulos.count()  # Se cuenta cuántos artículos hay
    img = Articulo.objects.filter(id=1)  # Imagen de la pestaña
    resta = articulos_count - 6  # Resta para artículos a mostrar

    # Verificación de si el usuario realiza una búsqueda
    search = request.GET.get('search')
    if search:
        articulo1 = articulos.filter(Q(tittle__icontains=search) | Q(tags__icontains=search) | Q(create__icontains=search)).distinct()
        # Renderización si el usuario realizó una búsqueda
        if cpu >= 80:
            context = {'search': articulo1, 'message_alert': message_alert, 'articulos': articulo1}
            return render(request, template_name, context)
        else:
            context = {'search': articulo1, 'articulos': articulo1}
            return render(request, template_name, context)

    # Renderización del template normalmente
    context = {'articulos': articulos, 'resta': resta, 'img': img}
    if cpu >= 80:
        context['message_alert'] = message_alert
    return render(request, template_name, context)



def ArticuloView(request, url: str, id: int):
    # Verificamos que el id solicitado sea correcto
    articulo_right = get_object_or_404(Articulo, pk=id, status=True)

    template_name = "blog/articulo/articulo.html"
    template_name_stop = "portafolio/stop.html"
    message_alert = True

    # Obtener datos externos
    UsuariosCap(request)
    cpu, memory = monitor_the_cpu_and_memory()
    cpu, memory = float(cpu), float(memory)

    # Guardar visita
    articulo = Articulo.objects.get(pk=id)
    articulo.visits += 1
    articulo.save()

    # Verificación de si el CPU está a más del 90%, en ese caso se renderiza el template_name_stop
    if cpu > 90:
        return render(request, template_name_stop)

    # Verificación de si el usuario realiza una búsqueda
    search = request.GET.get('search')
    if search:
        articulo1 = Articulo.objects.filter(
            Q(tittle__icontains=search) |
            Q(tags__icontains=search) |
            Q(create__icontains=search),
            status=True
        ).distinct()
        context = {'search': articulo1}
    else:
        context = {'articulo': articulo}
    
    return render(request, template_name, context)


def allView(request):
    template_name = "blog/all.html"
    template_name_stop = "portafolio/stop.html"
    message_alert = True

    # Obtener datos externos
    UsuariosCap(request)
    cpu, memory = monitor_the_cpu_and_memory()
    cpu, memory = float(cpu), float(memory)

    # Obtener registros de la base de datos
    articulos = Articulo.objects.filter(status=True).order_by('-id')
    no = 1

    # Verificación de si el CPU está a más del 90%, en ese caso se renderiza el template_name_stop
    if cpu > 90:
        return render(request, template_name_stop)

    # Retorno del template
    context = {'all': articulos, 'no': no}
    if cpu >= 80:
        context['message_alert'] = message_alert
    return render(request, template_name, context)


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
