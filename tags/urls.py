from django.urls import path

from tags.views import TagView

urlpatterns = [
    path('', TagView.as_view(), name='tag-list'),
]
