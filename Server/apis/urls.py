
# Importaciones de Django
from django.urls import path
from django.conf.urls import handler404, handler500

# Importaciones Propias
from .views import indexView, Error404, Error500

# Nombre de app
app_name = "myApis"

urlpatterns = [
    path('', indexView, name="indexView"), # Index de la app
]


# MANEJO DE ERRORES HTTP
handler404 = Error404 # Error 404
handler500 = Error500 # Error 500