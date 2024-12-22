from rest_framework.response import Response
from rest_framework.views import APIView

from categories.models import Category
from categories.serializers import CategoriesSerializer


class CategoryView(APIView):

    def get(cls, request):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)
