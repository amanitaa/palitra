from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment, Blog
from .permisions import IsOwner
from .serializers import CommentSerializer


class BlogCommentsView(APIView):
    def get(cls, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found."}, status=404)

        comments = Comment.objects.filter(blog=blog).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)


class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(cls, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class CommentUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def put(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found."}, status=404)

        self.check_object_permissions(request, comment)

        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class CommentDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found."}, status=404)

        self.check_object_permissions(request, comment)

        comment.delete()
        return Response({"message": "Comment deleted successfully."}, status=200)
