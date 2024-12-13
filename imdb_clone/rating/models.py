# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


# modelo para rating
class Rating(models.Model):
    movie = models.ForeignKey(Movie, related_name="ratings", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="ratings", on_delete=models.CASCADE)
    score = models.PositiveIntegerField()  # Calificación de 1 a 10, por ejemplo

    class Meta:
        unique_together = (
            "movie",
            "user",
        )

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}: {self.score}"
