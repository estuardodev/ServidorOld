from django.urls import path
from django.conf.urls import handler500, handler404

from . import views
from portafolio.views import AtributionView

app_name = 'criptosara'

urlpatterns = [
    path('', views.SaraIndexView.as_view(), name="saraindex"),
    path('terceros/', AtributionView.as_view(), name="atribucion")
]


handler500 = views.ErrorCripto500Views.as_view()
handler404 = views.ErrorCripto404Views.as_view()