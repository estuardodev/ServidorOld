
# Importaciones de Django
from django.urls import path
from django.conf.urls import handler404, handler500

# Importaciones Propias
from .views import indexView, Error404, Error500, getArticulo, getIPUsers

# Nombre de app
app_name = "myApis"

urlpatterns = [
    path('', indexView, name="indexView"), # Index de la app
    
    # API
    # Url para la api que obtiene un articulo mediante su pk
    path("articulo/<int:pk>", getArticulo, name="apiArticulo"),
    # Url para la api que obtiene la informacion de usuarios mediante su IP
    path("api/ip-users/<str:ip>", getIPUsers, name="apiIPUsers"),
]


# MANEJO DE ERRORES HTTP
handler404 = Error404 # Error 404
handler500 = Error500 # Error 500