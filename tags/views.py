from rest_framework.response import Response
from rest_framework.views import APIView

from tags.models import Tag
from tags.serializers import TagSerializer


class TagView(APIView):

    def get(cls, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
