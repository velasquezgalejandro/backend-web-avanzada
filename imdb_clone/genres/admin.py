# Register your models here.
from django.contrib import admin
from genres.models import Genre


# admin para Género
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Genre, GenreAdmin)
