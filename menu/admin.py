from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Menu


class MenuAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'location_number', 'category', 'link', 'order')
    list_editable = ('location_number', 'link')
    list_filter = ('category',)
    search_fields = ('title', 'category__name')


admin.site.register(Menu, MenuAdmin)
