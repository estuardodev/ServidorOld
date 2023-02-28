from django.contrib import admin
from .models import IPUsers

# Register your models here.

@admin.register(IPUsers)
class IPUsersModel(admin.ModelAdmin):
    '''With this model we can see the users that enter to the site'''
    list_display = ('ip', 'last_time', 'country', 'visits')
    search_fields = ('ip', 'browser','first_time', 'country', 'last_time')
    readonly_fields = ('ip', 'country', 'first_time', 'last_time', 'browser', 'visits', 'city', 'code_zip', 'lat', 'lon', 'isp')
