from django.urls import path

from . import views

app_name = "cripto"

urlpatterns = [
    path('', views.saraIndex, name="saraIndex")
]
