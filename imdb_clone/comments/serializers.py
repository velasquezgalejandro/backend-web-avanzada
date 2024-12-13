from rest_framework import serializers
from comments.models import Comment
from django.contrib.auth.models import User
from movies.models import Movie


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Comment
        fields = ["user", "movie", "content", "created_at", "updated_at"]

    def validate_content(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "El comentario debe tener al menos 5 caracteres."
            )
        return value
