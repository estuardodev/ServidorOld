from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from ipware import get_client_ip



# IndexView ("estuardodev.com" | "www.estuardodev.com")
def IndexView(request):
    template_name: str = "portafolio/index.html"
    
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_client = x_forwarded_for.split(',')[-1].strip() 
    else: 
        ip_client = request.META.get('REMOTE_ADDR') 

    return render(request, template_name, {'ip_client' : ip_client})
    
    

class Error404View(generic.TemplateView):
    template_name: str = "error/404.html"