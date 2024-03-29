from django.test import TestCase
from blog.models import Articulo
from django.urls import reverse

# Create your tests here.
class TestingOfTheApis(TestCase):
    '''Here the tests will be run to the urls of my apis'''

    def testGetArticuloResponse200(self):
        '''Probaremos si obtenemos un 200 al solicitar un articulo a mi API'''
        article = Articulo.objects.create(titulo="Test Tittle", contenido="Test Content", tags="Test1", 
                                          description="Test Description", url="/articulo/test",
                                          alt_imagen="Test Image", prioridad=0.9, autor="Test Autor")
        article.save()

        response = self.client.get(reverse("myApis:apiArticulo", args=[article.id]))
        self.assertEqual(response.status_code, 200)

    def testGetArticuloReponse404(self):
        '''Probaremos si obtenemos un 404 al solicitar un articulo que no existe a mi API'''
        response = self.client.get(reverse("myApis:apiArticulo", args=[10]))
        self.assertEqual(response.status_code, 404)

    def testGetCorrectInfoIP(self):
        '''Probaremos obtener la información de una IP que si existe (8.8.8.8) de Google'''
        response = self.client.get(reverse("myApis:apiIPUsers", args=["8.8.8.8"]))
        self.assertContains(response, "Success")

    def testGetIncorrectInfoIP(self):
        '''Probaremos obtener la información de una IP que no existe (222.20.1.) Inexistente por el punto'''
        response = self.client.get(reverse("myApis:apiIPUsers", args=["222.20.1."]))
        self.assertContains(response, "Fail")