from rest_framework import serializers
from movies.models import Movie
from actors.serializers import ActorSerializer
from directors.serializers import DirectorSerializer
from genres.serializers import GenreSerializer


# serializer para Pelicula
class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    director = DirectorSerializer()
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"
