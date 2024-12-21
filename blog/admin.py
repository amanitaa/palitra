from django.contrib import admin
from django.db import models

from tinymce.widgets import TinyMCE

from blog.models import Blog
from tags.models import Tag


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})}}
    list_display = ('title', 'author', 'category', 'created_at', 'active')
    list_filter = ('category', 'tags', 'active', 'created_at')
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',)


admin.site.register(Blog, BlogAdmin)
