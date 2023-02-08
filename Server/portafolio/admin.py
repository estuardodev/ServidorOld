from django.contrib import admin
from .models import IPClient, IPClientVisitas

# Register your models here.

class IPBlog(admin.ModelAdmin):
    list_display = ('id','ip_add')
    search_fields = ('id', 'ip_add')
    readonly_fields = ('id','ip_add')

admin.site.register(model_or_iterable=(IPClient), admin_class=IPBlog)

class VisitasBLog(admin.ModelAdmin):
    list_display = ('ip_key', 'visitas', 'ultima_vez')
    search_fields = ('id',)
    readonly_fields = ('id', 'ip_key', 'visitas', 'ultima_vez')

admin.site.register(model_or_iterable=(IPClientVisitas), admin_class=VisitasBLog)