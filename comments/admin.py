from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'author', 'content', 'parent', 'like', 'dislike', 'created_at')
    list_filter = ('blog', 'author', 'created_at')
    search_fields = ('content', 'author__username', 'blog__title')


admin.site.register(Comment, CommentAdmin)
