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
    path('articulo/Bienvenida/', views.BienvenidaView, name="BienvenidaView"),
    path('articulo/chatgpt3-la-herramienta-de-chatbot-mas-avanzada-de-openai', views.ChatGPT3View.as_view(), name="ChatGPT3View"),
    # SEO
    path('robots.txt', views.RobotsView.as_view()),
    path('sitemap.xml', views.SitemapView.as_view()),
    
    
    #path('BingSiteAuth.xml', TemplateView.as_view(template_name="portafolio/BingSiteAuth.xml", content_type="text/xml")),
]


# MANEJO DE ERRORES HTTP
handler404 = views.Error404.as_view() # Error 404
handler500 = views.Error500.as_view() # Error 500

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)