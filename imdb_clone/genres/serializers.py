from rest_framework import serializers
from genres.models import Genre


# Serializer para Género
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name", "description"]
