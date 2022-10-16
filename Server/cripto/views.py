from django.shortcuts import render
from django.http import HttpResponse

def saraIndex(request):
    return HttpResponse("Este es el subdominio")