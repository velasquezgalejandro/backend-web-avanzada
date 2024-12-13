# Create your views here.
from rest_framework import viewsets
from directors.models import Director
from directors.serializers import DirectorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Vista para Director
class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
