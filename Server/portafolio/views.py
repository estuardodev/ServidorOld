from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from ipware import get_client_ip


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
    
class AtributionView(generic.TemplateView):
    template_name: str = "terceros/atribucion.html"

class Error404View(generic.TemplateView):
    template_name: str = "error/404/404.html"

class Error500View(generic.TemplateView):
    template_name: str = "error/500/500.html"