from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "movie", "content", "created_at", "updated_at")
    search_fields = ("user__username", "movie__title", "content")
    list_filter = ("movie", "user")


admin.site.register(Comment, CommentAdmin)
