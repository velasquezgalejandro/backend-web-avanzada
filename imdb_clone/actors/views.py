from rest_framework import viewsets
from actors.models import Actor
from actors.serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Vista para Actor
class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
