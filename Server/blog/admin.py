from django.contrib import admin
from . import models

# Personalizacion de Administrador
admin.site.site_header = 'estuardodev'
admin.site.index_title = 'Panel de control de mi sitio'
admin.site.site_title = 'Administrador'
# Register your models here.


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'create', 'status')

    search_fields = ('tittle', 'create', 'autor', 'visits') 
    readonly_fields = ('visits',)
    fields = ('tittle', 'visits', 'description', 'tags', 'url', 'priority', 'content', 'image', 'alt_image', 'autor', 'status')
    

admin.site.register(models.Articulo, ArticuloAdmin)

class IPUsuariosAdmin(admin.ModelAdmin):
    list_display = ('ip', 'last_time', 'country', 'visits')
    search_fields = ('ip', 'browser','first_time', 'country', 'last_time')
    readonly_fields = ('ip', 'country', 'first_time', 'last_time', 'browser', 'visits', 'city', 'code_zip', 'lat', 'lon', 'isp')

admin.site.register(models.IPUsuarios, IPUsuariosAdmin)

