"""estuardodev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.views.generic.base import TemplateView

# Importaciones propias
from portafolio.views import Error404View, Error500View, AtributionView



urlpatterns = [
    # path('admin/', admin.site.urls),
    # Path sitios
    path('', include('portafolio.urls')),
    path('legal/', include('legal.urls')),
    path('terceros/', AtributionView.as_view()),

    #Path de archivos
    path('robots.txt', TemplateView.as_view(template_name="portafolio/robots.txt", content_type="text/plain")),
    path('sitemap.xml', TemplateView.as_view(template_name="portafolio/sitemap.xml", content_type="text/xml")),
    path('BingSiteAuth.xml', TemplateView.as_view(template_name="portafolio/BingSiteAuth.xml", content_type="text/xml")),
    path('app-ads.txt', TemplateView.as_view(template_name="portafolio/app-ads.txt", content_type="text/plain")),
    
]

# Error 404
handler404 = Error404View.as_view()

# Error 500
handler500 = Error500View.as_view()