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
        articulo = {'message': 'success', 'article': model_to_dict(visitas, exclude=['imagen', 'alt_imagen'])}
    except Articulo.DoesNotExist:
        articulo = {'message': 'Not Found'}

    return JsonResponse(articulo)

# ERRORES
def Error404(request, exception=None):
    response = {"message":"Error 404"}
    return JsonResponse(response)

def Error500(request):
    response = {"message":"Error 500"}
    return JsonResponse(response)