# Create your models here.
from django.db import models
from actors.models import Actor
from directors.models import Director
from genres.models import Genre


# modelo para Pelicula
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    poster = models.ImageField(
        upload_to="movie_posters/", blank=True, null=True
    )  # Campo para la imagen

    def __str__(self):
        return self.title
