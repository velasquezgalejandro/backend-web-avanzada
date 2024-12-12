# Create your views here.
# Vista para Género
from rest_framework import viewsets
from .models import Genre
from .serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
