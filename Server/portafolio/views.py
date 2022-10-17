from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from ipware import get_client_ip



# IndexView ("estuardodev.com" | "www.estuardodev.com")
def IndexView(request):
    template_name: str = "portafolio/index.html"
    ip_client, ip_boolean = get_client_ip(request)

    return render(request, template_name, {'ip_client' : ip_client})
    
    

class Error404View(generic.TemplateView):
    template_name: str = "error/404.html"