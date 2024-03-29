# DJANGO
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse

# MODULO PROPIO
from . import views
from .sitemaps import MapaDeSitio
from .feeds import UltimasNoticias

sitemaps = {
    'blog': MapaDeSitio
}

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    # SITIO
    path('', views.indexView),
    path('articulo/<str:url>/<int:id>', views.ArticuloView, name="ArticuloView"),
    path("all/", views.allView, name="all"),  

    # SEO
    path('robots.txt', views.RobotsView.as_view()),
    path('BingSiteAuth.xml', TemplateView.as_view(template_name="blog/BingSiteAuth.xml", content_type="text/xml")),
    path('feed/', UltimasNoticias()),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]


# MANEJO DE ERRORES HTTP
handler404 = views.Error404 # Error 404
handler500 = views.Error500 # Error 500
