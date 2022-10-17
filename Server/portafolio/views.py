from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from ipware import get_client_ip



# IndexView ("estuardodev.com" | "www.estuardodev.com")
def IndexView(request):
    template_name: str = "portafolio/index.html"
    
    client_ip, is_routable = get_client_ip(request)
    if client_ip is None:
        ip_client = 'NO SE HA LOGRADO CAPTURAR TU IP'
    else:
        ip_client = client_ip
    if is_routable:
        ip_client = client_ip
    else:
        ip_client = client_ip

    return render(request, template_name, {'ip_client' : ip_client})
    
    

class Error404View(generic.TemplateView):
    template_name: str = "error/404.html"