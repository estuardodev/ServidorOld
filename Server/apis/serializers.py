from rest_framework import serializers
from blog.models import Articulo

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('id', 'titulo', 'visits', 'contenido', 'tags', 'description', 'real_url', 'creado_el', 
                'creado', 'alt_imagen', 'prioridad', 'autor')
        read_only_fields = ('id', 'titulo', 'visits', 'contenido', 'tags', 'description', 'url', 'creado_el', 
                'creado', 'alt_imagen', 'prioridad', 'autor')
        