from django.contrib.syndication.views import Feed, FeedGenerator
from .models import Articulo

class UltimasNoticiasFeed(Feed):
    title = "Ciencia y Tecnología"
    link = "/feed/"
    description = "Mantente actualizado con las últimas noticias y análisis de nuestro equipo técnico. Desde política hasta entretenimiento, cubrimos todo lo que necesitas saber en nuestro blog de noticias actualizado diariamente."

    def items(self):
        return Articulo.objects.order_by('-id')[:8]

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.contenido

    def item_link(self, item):
        return f"{item.url}/{item.id}/"
