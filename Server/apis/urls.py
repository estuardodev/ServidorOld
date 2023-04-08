
# Importaciones de Django
from django.urls import path
from django.conf.urls import handler404, handler500

# Importaciones Propias
from .views import indexView, Error404, Error500, getArticulo, getIPUsers
from .api import ProjectViewSet

# Importaciones externas
from rest_framework import routers

# Nombre de app
app_name = "myApis"

# ROUTER DE REST
router = routers.DefaultRouter()
router.register('articulo',ProjectViewSet, "apiArticulo")

urlpatterns = [
    path('', indexView, name="indexView"), # Index de la app
    
    # API
    # Url para la api que obtiene la informacion de usuarios mediante su IP
    path("ip-users/<str:ip>", getIPUsers, name="apiIPUsers"),
] + router.urls


# MANEJO DE ERRORES HTTP
handler404 = Error404 # Error 404
handler500 = Error500 # Error 500