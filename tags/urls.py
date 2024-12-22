from django.urls import path

from tags.views import TagView

app_name = 'tags'

urlpatterns = [
    path('', TagView.as_view(), name='tag-list'),
]
