# Register your models here.
from django.contrib import admin
from rating.models import Rating


# admin para Rating
class RatingAdmin(admin.ModelAdmin):
    list_display = ("movie", "user", "score")
    search_fields = ("movie", "user")


admin.site.register(Rating, RatingAdmin)
