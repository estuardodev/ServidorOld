# Importaciones de Django
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Importaciones Propias


# Create your views here.
def indexView(request):
    response = {"message":"Success"}
    return JsonResponse(response)