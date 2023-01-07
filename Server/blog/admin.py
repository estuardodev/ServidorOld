from django.contrib import admin
from . import models

# Personalizacion de Administrador
admin.site.site_header = 'estuardodev'
admin.site.index_title = 'Panel de control de mi sitio'
admin.site.site_title = 'Administrador'
# Register your models here.


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'creado')

    search_fields = ('titulo', 'creado')
    fields = ('titulo', 'description', 'tags', 'url', 'prioridad', 'contenido', 'imagen', 'alt_imagen')

admin.site.register(models.Articulo, ArticuloAdmin)

class IPUsuariosAdmin(admin.ModelAdmin):
    list_display = ('ip', 'last_visit', 'visits')
    search_fields = ('ip', 'one_visit', 'navigator', 'last_visit', 'visits', 'code_status')
    readonly_fields = ('ip', 'visits', 'last_visit', 'one_visit', 'navigator', 'code_status')

admin.site.register(models.IPUsuarios, IPUsuariosAdmin)