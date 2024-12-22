from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.serializers import CategoriesSerializer


class CategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(cls, request):
        serializer = CategoriesSerializer(request.user, many=True)
        return Response(serializer.data)
