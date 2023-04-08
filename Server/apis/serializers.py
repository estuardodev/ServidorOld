from rest_framework import serializers
from blog.models import Articulo

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('id', 'tittle', 'visits', 'content', 'tags', 'description', 'real_url', 'date_create', 
                'create', 'alt_image', 'priority', 'autor')
        read_only_fields = ('id', 'tittle', 'visits', 'content', 'tags', 'description', 'url', 'date_create', 
                'create', 'alt_image', 'priority', 'autor')
        