# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comentario de {self.user.username} en {self.movie.title}"

    class Meta:
        ordering = ["-created_at"]
