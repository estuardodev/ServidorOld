from django.db import models

# Create your models here.
class IPUsers(models.Model):
    '''This Table of the Database save the data basic of the users'''
    ip = models.CharField(primary_key=True, db_column="IP", verbose_name="IP_ID", max_length=255)
    browser = models.CharField(verbose_name="Browser", max_length=255, db_column="Browser")
    first_time = models.DateTimeField(verbose_name="First Time", auto_now_add=True, db_column="First Time")
    last_time = models.DateTimeField(verbose_name="Last Time", auto_now=True, db_column="Last Time")
    visits = models.IntegerField(verbose_name="Visits", default=0, db_column="Visits")

    def __str__(self):
        return self.ip
    
    class Meta:
        verbose_name = "IP Users"
        verbose_name_plural = "IP Users"
    