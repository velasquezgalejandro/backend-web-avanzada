from rest_framework import serializers
from movies.models import Movie
from rating.models import Rating
from django.contrib.auth.models import User


# serializer para Rating
class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Rating
        fields = ["movie", "user", "score"]

    def validate_score(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError(
                "La calificación debe estar entre 1 y 10."
            )
        return value
