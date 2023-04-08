from rest_framework import viewsets, permissions
from blog.models import Articulo
from .serializers import ProjectSerializers

class ProjectViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Articulo.objects.all().order_by("-id")
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializers