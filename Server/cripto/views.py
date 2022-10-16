from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

class SaraIndexView(generic.TemplateView):
    template_name: str = "cripto/sara.html"