from django.db import models

# Create your models here.
class IPUsers(models.Model):
    '''This Table of the Database save the data basic of the users'''
    ip = models.CharField(primary_key=True, db_column="IP", verbose_name="IP_ID", max_length=255)
    country = models.CharField(verbose_name="Country", max_length=255, db_column="Country", null=True)
    first_time = models.DateTimeField(verbose_name="First Time", auto_now_add=True, db_column="First Time")
    last_time = models.DateTimeField(verbose_name="Last Time", auto_now=True, db_column="Last Time")
    browser = models.CharField(verbose_name="Browser", max_length=255, db_column="Browser")
    visits = models.IntegerField(verbose_name="Visits", default=0, db_column="Visits")
    city = models.CharField(max_length=255, verbose_name="City", db_column="City", null=True)
    code_zip = models.CharField(max_length=60, verbose_name="Code Postal", db_column="CodePostal", null=True)
    lat = models.CharField(max_length=255, verbose_name="Latitude", db_column="latitude", null=True)
    lon = models.CharField(max_length=255, verbose_name="Longitude", db_column="langitude", null=True)
    isp = models.CharField(max_length=255, verbose_name="ISP", db_column="ISP", null=True)
    

    def __str__(self):
        return self.ip
    
    class Meta:
        verbose_name = "IP Users"
        verbose_name_plural = "IP Users"
    