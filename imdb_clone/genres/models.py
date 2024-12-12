from django.db import models


# Create your models here.
# Modelo para Género
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
