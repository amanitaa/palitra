from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from categories.models import Category


class Menu(models.Model):
    title = models.CharField(max_length=200)
    location_number = models.PositiveIntegerField()
    category = TreeForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='menus')
    link = models.URLField(null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
