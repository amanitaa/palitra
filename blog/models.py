from django.db import models

from categories.models import Category
from tags.models import Tag
from user.models import User


class Blog(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='blog_images/')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
