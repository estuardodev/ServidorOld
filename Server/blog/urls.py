# DJANGO
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static

# MODULO PROPIO
from . import views

urlpatterns = [
    # SITIO
    path('', views.indexView, name='IndexView'),

    # SEO
    path('robots.txt', TemplateView.as_view(template_name="blog/robots.txt", content_type="text/plain")),
    path('ads.txt', TemplateView.as_view(template_name="blog/ads.txt", content_type="text/plain")),
    path('sitemap.xml', TemplateView.as_view(template_name="blog/sitemap.xml", content_type="text/xml")),
    #path('BingSiteAuth.xml', TemplateView.as_view(template_name="portafolio/BingSiteAuth.xml", content_type="text/xml")),
]


# MANEJO DE ERRORES HTTP
handler404 = views.Error404.as_view() # Error 404
handler500 = views.Error500.as_view() # Error 500

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)