from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField(max_length=5000)
    tags = models.CharField(max_length=400, null=True)
    description = models.CharField(max_length=360, null=True)
    url = models.CharField(max_length=500)
    creado_el = models.DateTimeField(auto_now_add=True, null=True)
    creado = models.DateField(auto_now_add=True, null=True)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    alt_imagen = models.CharField(max_length=150, null=True)
    prioridad = models.FloatField(default=0.5)

    def __str__(self) -> str:
        return self.titulo + " ID: " + str(self.id)
