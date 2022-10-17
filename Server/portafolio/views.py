from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# IndexView ("estuardodev.com" | "www.estuardodev.com")
class IndexView(generic.TemplateView):
    template_name: str = "portafolio/index.html"

class Error404View(generic.TemplateView):
    template_name: str = "error/404.html"