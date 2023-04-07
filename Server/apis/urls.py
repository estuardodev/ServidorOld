
# Importaciones de Django
from django.urls import path

# Importaciones Propias
from .views import indexView

# Nombre de app
app_name = "myApis"

urlpatterns = [
    path('', indexView, name="indexView"), # Index de la app
]
