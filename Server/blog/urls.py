# DJANGO
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static

# MODULO PROPIO
from . import views

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    # SITIO
    path('', views.indexView, name='IndexView'),
    path('articulo/<str:url>/<int:id>', views.ArticuloView, name="ArticuloView"),
    

    # SEO
    path('robots.txt', views.RobotsView.as_view()),
    path('sitemap.xml', views.SitemapView.as_view()),
    path('BingSiteAuth.xml', TemplateView.as_view(template_name="blog/BingSiteAuth.xml", content_type="text/xml")),
]


# MANEJO DE ERRORES HTTP
handler404 = views.Error404.as_view() # Error 404
handler500 = views.Error500.as_view() # Error 500
