# Importaciones de Python
import requests

# Importaciones de Django
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

# Importaciones Propias
from blog.models import Articulo

# Create your views here.
def indexView(request):
    response = {"message":"Success"}
    return JsonResponse(response)

# API que permite obtener un articulo de mi blog
def getArticulo(request, pk:int):
    try:
        visitas = Articulo.objects.get(id=pk)
        articulo = {'message': 'Success', 'article': model_to_dict(visitas, exclude=['imagen', 'alt_imagen'])}
    except Articulo.DoesNotExist:
        articulo = {'message': 'Not Found'}

    return JsonResponse(articulo)

# API que permite obtener informacion de los usuarios acerca de su IP
def getIPUsers(request, ip:str):
    try:
        petition = requests.get(f"http://ip-api.com/json/{ip}")
        petition = petition.json()
        information = {'message': 'Success', 'information': petition}
    except Articulo.DoesNotExist:
        information = {'message': 'Not Found'}

    return JsonResponse(information)

# ERRORES
def Error404(request, exception=None):
    response = {"message":"Error 404"}
    return JsonResponse(response)

def Error500(request):
    response = {"message":"Error 500"}
    return JsonResponse(response)