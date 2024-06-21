from rest_framework import viewsets
from .models import World
from .serializers import WorldSerializer
from rest_framework.permissions import AllowAny  # Change this import

class WorldViewSet(viewsets.ModelViewSet):
    queryset = World.objects.all()
    serializer_class = WorldSerializer
    permission_classes = [AllowAny]