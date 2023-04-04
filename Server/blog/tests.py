# Importaciones de Python
import requests

# Importaciones de Django
from django.test import TestCase, Client

# Importación de mis models
from .models import Articulo

# Create your tests here.
# NOTA: Para ejecutar los test del blog en un entorno local, el servidor debe estar ejecutandose

class TestingOfCodeStatusOfTheArticles(TestCase):
    '''This testing is for see if work all code status of the blog'''

    def setUp(self):
        self.articulo = Articulo.objects.create(
            titulo='Prueba',
            contenido='Prueba',
            tags='Prueba',
            description='Prueba',
            url='/articulo/test',
            alt_imagen='Prueba',
            prioridad=0.9,
            autor='Prueba'
        )

    def testCodeStatus200(self):
            '''Test of the code status 200 in articles existent'''
            # URL a testear
            url = f'http://blog.estuardodev.com:8000/articulo/test/1'

            # Hace la petición GET a la vista del artículo
            response = requests.get(url)

            # Verifica que la respuesta sea exitosa
            self.assertEqual(response.status_code, 200)

    def testCodeStatus404(self):
            '''Test of the code status 404 in articles inexistent'''
            # URL a testear
            url = f'http://blog.estuardodev.com:8000/articulo/test/1000'

            # Hace la petición GET a la vista del artículo
            response = requests.get(url)

            # Verifica que la respuesta sea 404
            self.assertEqual(response.status_code, 404)
        