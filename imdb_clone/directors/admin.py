# Register your models here.
from django.contrib import admin
from directors.models import Director


# admin para Director
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_date")
    search_fields = ("name",)


admin.site.register(Director, DirectorAdmin)
