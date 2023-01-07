from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField(max_length=5000)
    tags = models.CharField(max_length=400, null=True)
    description = models.TextField(max_length=360, null=True)
    url = models.CharField(max_length=500)
    creado_el = models.DateTimeField(auto_now_add=True, null=True)
    creado = models.DateField(auto_now_add=True, null=True)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    alt_imagen = models.CharField(max_length=150, null=True)
    prioridad = models.FloatField(default=0.5)

    def __str__(self) -> str:
        return self.titulo + " ID: " + str(self.id)

class IPUsuarios(models.Model):
    ip = models.CharField(max_length=200, verbose_name="IP del Usuario", null=True)
    navigator = models.CharField(max_length=256, verbose_name="Navegador, OS y más", null=True)
    one_visit = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Primer Visita")
    last_visit = models.DateTimeField(auto_now=True, null=True, verbose_name="Última Visita")
    visits = models.IntegerField(default=0, verbose_name="Total de Visitas", null=True)
    code_status = models.IntegerField(default=0, verbose_name="Codigo de respuesta", null=True)
    
    def __str__(self) -> str:
        return self.ip

    class Meta:
        verbose_name = "Usuarios IP"
        verbose_name_plural = "Usuarios IP"
        
