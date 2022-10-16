from django.urls import path

from . import views

app_name = 'criptosara'

urlpatterns = [
    path('', views.SaraIndexView.as_view(), name="saraindex"),
]
