from django.urls import path
from django.conf.urls import handler404

from . import views
from portafolio.views import AtributionView, Error404View

app_name = 'criptosara'

urlpatterns = [
    path('', views.SaraIndexView.as_view(), name="saraindex"),
    path('terceros/', AtributionView.as_view(), name="atribucion")
]

handler404 = Error404View.as_view()