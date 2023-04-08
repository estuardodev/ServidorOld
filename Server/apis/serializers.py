from rest_framework import serializers
from blog.models import Articulo

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('id', 'tittle', 'description', 'tags',  'real_url', 'real_url_image', 'alt_image', 'priority', 'content', 
                'date_create', 'autor', 'visits')
        
        