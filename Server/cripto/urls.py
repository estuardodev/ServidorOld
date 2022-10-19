from django.urls import path
from django.conf.urls import handler500, handler404
from django.views.generic.base import TemplateView

from . import views
from portafolio.views import AtributionView

app_name = 'criptosara'

urlpatterns = [
    path('', views.SaraIndexView.as_view(), name="saraindex"),
    path('terceros/', AtributionView.as_view(), name="atribucion"),
    path('robots.txt', TemplateView.as_view(template_name="portafolio/robots.txt", content_type="text/plain")),
    path('sitemap.xml', TemplateView.as_view(template_name="portafolio/sitemap.xml", content_type="text/xml")),
    path('BingSiteAuth.xml', TemplateView.as_view(template_name="portafolio/BingSiteAuth.xml", content_type="text/xml")),
]


handler500 = views.ErrorCripto500Views.as_view()
handler404 = views.ErrorCripto404Views.as_view()