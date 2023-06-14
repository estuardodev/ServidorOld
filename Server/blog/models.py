from django.db import models

# Create your models here.
class Articulo(models.Model):
    tittle = models.CharField(max_length=150)
    description = models.TextField(max_length=360, null=True)
    tags = models.CharField(max_length=400, null=True)
    url = models.CharField(max_length=500)
    priority = models.FloatField(default=0.5)
    content = models.TextField(max_length=5000)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    create = models.DateField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    alt_image = models.CharField(max_length=150, null=True)
    autor = models.CharField(max_length=200, default='Estuardo Ramírez')
    visits = models.IntegerField(default=0, verbose_name="Total Visitas", null=True) 
    status = models.BooleanField(default=True, verbose_name="Estado")  

    def __str__(self) -> str:
        return self.tittle + " ID: " + str(self.id)
    
    def real_url(self) -> str:
        return f"http://blog.estuardodev.com{self.url}/{self.id}"
    
    def real_url_image(self) -> str:
        return f"http://blog.estuardodev.com/media/{self.image}"
    

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
        
