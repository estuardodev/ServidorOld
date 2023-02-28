from django.db import models

# Create your models here.
class Articulo(models.Model):
    visits = models.IntegerField(default=0, verbose_name="Total Visitas", null=True)
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
    autor = models.CharField(max_length=200, default='Estuardo Ramírez')
    

    def __str__(self) -> str:
        return self.titulo + " ID: " + str(self.id)

class IPUsuarios(models.Model):
    ip = models.CharField(max_length=200, verbose_name="IP del Usuario", null=True)
    country = models.CharField(verbose_name="Country", max_length=255, db_column="Country", null=True)
    first_time = models.DateTimeField(verbose_name="First Time", auto_now_add=True, db_column="First Time", null=True)
    last_time = models.DateTimeField(verbose_name="Last Time", auto_now=True, db_column="Last Time", null=True)
    browser = models.CharField(verbose_name="Browser", max_length=255, db_column="Browser", null=True)
    visits = models.IntegerField(verbose_name="Visits", default=0, db_column="Visits", null=True)
    city = models.CharField(max_length=255, verbose_name="City", db_column="City", null=True)
    code_zip = models.CharField(max_length=60, verbose_name="Code Postal", db_column="CodePostal", null=True)
    lat = models.CharField(max_length=255, verbose_name="Latitude", db_column="latitude", null=True)
    lon = models.CharField(max_length=255, verbose_name="Longitude", db_column="langitude", null=True)
    isp = models.CharField(max_length=255, verbose_name="ISP", db_column="ISP", null=True)
    
    def __str__(self) -> str:
        return self.ip

    class Meta:
        verbose_name = "Usuarios IP"
        verbose_name_plural = "Usuarios IP"
        
