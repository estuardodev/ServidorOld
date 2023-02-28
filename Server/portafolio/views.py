# Imports the systen
import os, mimetypes, time

# Imports the Django
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic

# Imports the third party
from ipware import get_client_ip
from psutil import cpu_percent, virtual_memory

# Imports the my moduls
from .models import IPClient, IPClientVisitas
# Arreglado


def get_user_public_ip(request):
    """  Getting client Ip  """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip() 
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def monitor_the_cpu_and_memory():
    cpu = cpu_percent()
    memory = virtual_memory().percent
    return cpu, memory
 

# IndexView ("estuardodev.com" | "www.estuardodev.com")
def IndexView(request):
    template_name: str = "portafolio/index.html"
    template_name_stop: str = "portafolio/stop.html"
    
    ip_client = get_user_public_ip(request)
    cpu, memory = monitor_the_cpu_and_memory()
    cpu, memory = float(cpu), float(memory)

    message_alert = True
    try:
        cliente = IPClient.objects.get(ip_add=ip_client)
        selected_client = cliente.ipclientvisitas_set.get(pk=cliente.id)
        selected_client.visitas += 1
        selected_client.save()
        
    except IPClient.DoesNotExist:
        create = IPClient.objects.create(ip_add=ip_client)
        create.save()
        create.ipclientvisitas_set.create(visitas=1)

    if cpu > 90:
        return render(request, template_name_stop)
    elif cpu >= 80:
        return render(request, template_name, {'ip_client' : ip_client, 'message_alert': message_alert})
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
    filename = '2023' + '-' + '02' + '-' + '07' + '-' + 'django_app' +'.sql'
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


class YouTubeView(generic.TemplateView):
    template_name: str = "portafolio/youtube/yt.html"    
    
class AtributionView(generic.TemplateView):
    template_name: str = "terceros/atribucion.html"

class Error404View(generic.TemplateView):
    template_name: str = "error/404/404.html"

class Error500View(generic.TemplateView):
    template_name: str = "error/500/500.html"