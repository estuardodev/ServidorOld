# Imports the systen
import os, mimetypes, requests

# Imports the Django
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic
from django.utils import timezone


# Imports the third party
from ipware import get_client_ip
from psutil import cpu_percent, virtual_memory

# Imports the my moduls
from .models import IPUsers
# Arreglado


def data_users(request):
    '''With this function recolect and save the information of the users'''
    ip, v_f = get_client_ip(request)
    user_agent = request.headers['User-Agent']
    petition = requests.get(f"http://ip-api.com/json/{ip}")
    petition = petition.json()
    if petition['status'] == "success":
    
        try:
            # Save IPUsers
            cliente = IPUsers.objects.get(ip=ip)
            cliente.browser = user_agent
            cliente.country = petition['country']
            cliente.city = petition['city']
            cliente.lat = petition['lat']
            cliente.lon = petition['lon']
            cliente.code_zip = petition['zip']
            cliente.isp = petition['isp']
            cliente.visits += 1
            cliente.save()
            
        except (IPUsers.DoesNotExist):
            create = IPUsers.objects.create(
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
            cliente = IPUsers.objects.get(ip=ip)
            cliente.browser = user_agent
            cliente.country = "LocalHost",
            cliente.city = "LocalHost",
            cliente.lat = "LocalHost",
            cliente.lon = "LocalHost",
            cliente.code_zip = "LocalHost",
            cliente.isp = "LocalHost",
            cliente.visits += 1
            cliente.save()
            
        except IPUsers.DoesNotExist:
            create = IPUsers.objects.create(
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

def monitor_the_cpu_and_memory():
    '''With this function we monitor the data the system'''
    cpu = cpu_percent()
    memory = virtual_memory().percent
    return cpu, memory
 

# IndexView ("estuardodev.com" | "www.estuardodev.com")
def IndexView(request):
    return HttpResponse("El Sitio No Está Disponible Por El Momento, Estamos en Migración")
    template_name: str = "portafolio/index.html"
    template_name_stop: str = "portafolio/stop.html"
    
    ip_client, user_agent = data_users(request)
    cpu, memory = monitor_the_cpu_and_memory()
    cpu, memory = float(cpu), float(memory)
    
    if cpu > 90:
        return render(request, template_name_stop)
    elif cpu >= 80:
        return render(request, template_name, {'ip_client' : ip_client, 'message_alert': True})
    else:
        return render(request, template_name, {'ip_client' : ip_client})

def DownloadView(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'CV-2023.png'
    # Define the full file path
    filepath = BASE_DIR + '/static/files/' + filename
    # Open the file for reading content
    path = open(filepath, 'rb').read()
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

def DownloadDBView(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'django_sql' +'.sql'
    # Define the full file path
    filepath = BASE_DIR + '/copy_db/' + filename
    # Open the file for reading content
    path = open(filepath, 'rb').read()
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response  
    
class AtributionView(generic.TemplateView):
    template_name: str = "terceros/atribucion.html"

class Error404View(generic.TemplateView):
    template_name: str = "error/404/404.html"

class Error500View(generic.TemplateView):
    template_name: str = "error/500/500.html"

''' SUSPENDED
class YouTubeView(generic.TemplateView):
    template_name: str = "portafolio/youtube/yt.html"  
'''
