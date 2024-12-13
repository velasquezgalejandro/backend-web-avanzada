# Create your models here.
from django.db import models


# modelo para Director
class Director(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
