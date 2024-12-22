from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from tags.serializers import TagSerializer


class TagView(APIView):
    permission_classes = [IsAuthenticated]

    def get(cls, request):
        serializer = TagSerializer(request.user, many=True)
        return Response(serializer.data)
