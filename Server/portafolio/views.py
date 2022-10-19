from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic
from ipware import get_client_ip
from .models import IPClient, IPClientVisitas


def get_user_public_ip(request):
    """  Getting client Ip  """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip() 
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# IndexView ("estuardodev.com" | "www.estuardodev.com")
def IndexView(request):
    template_name: str = "portafolio/index.html"
    
    ip_client = get_user_public_ip(request)

    return render(request, template_name, {'ip_client' : ip_client})
'''  
    try:
        cliente = IPClient.objects.get(ip_add=ip_client)
        selected_client = cliente.ipclientvisitas_set.get(pk=cliente.id)
        selected_client.visitas += 1
        selected_client.save()
        
    except IPClient.DoesNotExist:
        create = IPClient.objects.create(ip_add=ip_client)
        create.save()
        create.ipclientvisitas_set.create(visitas=1)
 '''   

    
    
class AtributionView(generic.TemplateView):
    template_name: str = "terceros/atribucion.html"

class Error404View(generic.TemplateView):
    template_name: str = "error/404/404.html"

class Error500View(generic.TemplateView):
    template_name: str = "error/500/500.html"