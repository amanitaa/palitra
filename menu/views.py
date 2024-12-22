from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from menu.serializers import MenuSerializer


class MenuView(APIView):
    permission_classes = [IsAuthenticated]

    def get(cls, request):
        serializer = MenuSerializer(request.user, many=True)
        return Response(serializer.data)
