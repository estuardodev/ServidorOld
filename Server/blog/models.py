from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField(max_length=5000)
    url = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    alt_image = models.CharField(max_length=150, null=True)

    def __str__(self) -> str:
        return self.titulo