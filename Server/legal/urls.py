from django.urls import path

# Importación de la misma carpeta
from . import views

# Nombre de app
app_name = 'legal'

urlpatterns = [
    path('politicas-de-privacidad/', views.PoliticasView, name="politicas"),
    path('terminos-y-condiciones/', views.TerminosView, name="terminos"),
    path('cookies/', views.CookiesView, name="cookies"),
]
