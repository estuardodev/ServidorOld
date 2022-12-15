from django.shortcuts import render
from django.http import HttpResponse # Respuesta HTTP

# Create your views here.
def indexView(request):
    return HttpResponse('HOLA MUNDO')