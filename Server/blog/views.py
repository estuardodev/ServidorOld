from django.shortcuts import render
from django.http import HttpResponse # Respuesta HTTP
from django.views import generic

# Create your views here.
def indexView(request):
    return render(request, 'blog/index.html')

class Error404(generic.TemplateView):
    template_name: str = "error/404/404.html"

class Error500(generic.TemplateView):
    template_name: str = "error/500/500.html"