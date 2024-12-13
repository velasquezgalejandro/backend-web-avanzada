# Create your views here.
from rest_framework import viewsets
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# from movies.permissions import IsOwnerOrReadOnly


# vista para Pelicula
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
