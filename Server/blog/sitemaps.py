from django.contrib.sitemaps import Sitemap
from .models import Articulo

class MapaDeSitio(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'
    def items(self):
        return Articulo.objects.all()
    def lastmod(self, obj):
        return obj.creado
        
    def location(self,obj):
        return '%s' % (obj.url)