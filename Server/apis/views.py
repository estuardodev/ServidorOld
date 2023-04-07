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
    response = {
        "message":"Success, these are the available APIs",
        "getArticulo":"With this API you get information about any of my articles with the id you request. URL: estuardodev.com/api/articulo/<id>",
        "getIPUsers":"With this API you get information about the IP address you designate in the url. URL: estuardodev.com/api/ip-users/<ip>"
        }
    return JsonResponse(response)

# API que permite obtener un articulo de mi blog
def getArticulo(request, pk:int):
    try:
        visitas = Articulo.objects.get(id=pk)
        articulo = {'message': 'Success', 'article': model_to_dict(visitas, exclude=['imagen', 'alt_imagen'])}
    except Articulo.DoesNotExist:
        articulo = {'message': 'Not Found'}
        return JsonResponse(articulo, status=404)

    return JsonResponse(articulo)

# API que permite obtener informacion de los usuarios acerca de su IP
def getIPUsers(request, ip:str):
    # Realizamos una peticion al servicio de http://ip-api.com
    petition = requests.get(f"http://ip-api.com/json/{ip}")
    petition = petition.json()
    
    # Realizamos la validación de la información que nos devuelve la petición
    # De ser success entonces lo acoplamos a nuestra forma y eliminamos su mensaje
    if petition["status"] == "success":
        del petition["status"]
        information = {'message': 'Success', 'information': petition}
    elif petition["status"] == "fail": # De ser fail, lo acoplamos a nuestra forma y eliminamos su mensaje
        del petition["status"]
        information = {'message': 'Fail', 'information': petition}
    else: # De no cumplirse por si dado caso cambien los mensajes, entonces mostrara la informacion normal sin alterar
        information = {'message': 'Success', 'information': petition}    

    return JsonResponse(information)

# ERRORES
def Error404(request, exception=None):
    response = {"message":"Error 404"}
    return JsonResponse(response)

def Error500(request):
    response = {"message":"Error 500"}
    return JsonResponse(response)