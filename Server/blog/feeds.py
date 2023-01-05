from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Articulo
import urllib.request

class UltimasNoticias(Feed):
    title = "Ciencia y Tecnología"
    link = "/feed/"
    description = "Mantente actualizado con las últimas noticias y análisis de nuestro equipo técnico. Desde política hasta entretenimiento, cubrimos todo lo que necesitas saber en nuestro blog de noticias actualizado diariamente."
    language = "es-GT"

    def items(self):
        return Articulo.objects.order_by('-id')[:9]

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.description

    def item_pubdate(self, item):
        return item.creado_el

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return f'{item.url}/{item.id}'

    
    # IMAGENES
    def item_enclosure_mime_type(self, item):
        return "image/webp"

    def item_enclosure_url(self, item):
        return f'https://blog.estuardodev.com/media/{item.imagen}'

    def item_enclosure_length(self, item):
        try:
            response = urllib.request.urlopen(f'https://blog.estuardodev.com/media/{item.image}')
            return int(response.info()["Content-Length"])
        except urllib.error.HTTPError:
            return 0