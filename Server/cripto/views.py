from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

class SaraIndexView(generic.TemplateView):
    template_name: str = "cripto/sara.html"

class RobotsView(generic.TemplateView):
    template_name: str = "cripto/robots.txt"
    content_type = 'text/plain'

class ErrorCripto404Views(generic.TemplateView):
    template_name: str = "cripto/error/404/404.html"

class ErrorCripto500Views(generic.TemplateView):
    template_name: str = "cripto/error/500/500.html"