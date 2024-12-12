# Register your models here.
from django.contrib import admin
from actors.models import Actor


# Admin para Actor
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_date")
    search_fields = ("name",)


admin.site.register(Actor, ActorAdmin)
