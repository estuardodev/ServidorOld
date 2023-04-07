# Importaciones de Django
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Importaciones Propias


# Create your views here.
def indexView(request):
    response = {"message":"Success"}
    return JsonResponse(response)

# ERRORES
def Error404(request):
    response = {"message":"Error 404"}
    return JsonResponse(response)

def Error500(request):
    response = {"message":"Error 500"}
    return JsonResponse(response)