from django.urls import path
from . import views

app_name = 'portafolio'

urlpatterns = [
    path('', views.IndexView, name="index")
]
