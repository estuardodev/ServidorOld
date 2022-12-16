from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(max_length=2000)
    url = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    alt_image = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.titulo