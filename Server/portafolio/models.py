from django.db import models

# Create your models here.
class IPClient(models.Model):
    ip_add = models.CharField(max_length=200, verbose_name="IP del Usuario")

    def __str__(self):
        return self.ip_add

    class Meta:
        verbose_name = "IP CLientes"
        verbose_name_plural = "IP Clientes"

class IPClientVisitas(models.Model):
    ip_key = models.ForeignKey(IPClient, on_delete=models.CASCADE, verbose_name="Direccion IP")
    visitas = models.IntegerField(default=0, verbose_name="Visitas del Usuario")

    class Meta:
        verbose_name = "Visitas de IP"
        verbose_name_plural = "Visitas de IP"