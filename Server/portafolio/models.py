from django.db import models

# Create your models here.
class IPClient(models.Model):
    ip_add = models.CharField(max_length=200)

    def __str__(self):
        return self.ip_add

class IPClientVisitas(models.Model):
    ip_key = models.ForeignKey(IPClient, on_delete=models.CASCADE)
    visitas = models.IntegerField(default=0)