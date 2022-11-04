from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse

# Create your views here.
def TerminosView(request):
    url_name:str = 'Estuardo Ramírez'
    template_name:str = 'legal/terminos.html'

    return render(request, template_name, {'url_name':url_name})

def PoliticasView(request):
    url_name:str = 'Estuardo Ramírez'
    template_name:str = 'legal/politicas.html'

    return render(request, template_name, {'url_name':url_name})

def CookiesView(request):
    url_name:str = 'Estuardo Ramírez'
    template_name:str = 'legal/cookies.html'

    return render(request, template_name, {'url_name':url_name})
