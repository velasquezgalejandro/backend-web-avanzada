# Register your models here.
from django.contrib import admin
from movies.models import Movie


# admin para Movie
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "release_date", "director")
    search_fields = ("title", "description")
    list_filter = ("release_date", "director")


admin.site.register(Movie, MovieAdmin)
