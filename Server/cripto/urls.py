from django.urls import path

from . import views
from portafolio.views import AtributionView

app_name = 'criptosara'

urlpatterns = [
    path('', views.SaraIndexView.as_view(), name="saraindex"),
    path('terceros/', AtributionView.as_view(), name="atribucion")
]
