from rest_framework.response import Response
from rest_framework.views import APIView

from menu.models import Menu
from menu.serializers import MenuSerializer


class MenuView(APIView):

    def get(cls, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)
