from django.urls import path
from .views import BlogCommentsView, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('blogs/<int:blog_id>/comments/', BlogCommentsView.as_view(), name='blog-comments'),
    path('', CommentCreateView.as_view(), name='comment-create'),
    path('<int:comment_id>/', CommentUpdateView.as_view(), name='comment-update'),
    path('<int:comment_id>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
