from django.urls import path

from menu.views import MenuView

app_name = 'menu'

urlpatterns = [
    path('', MenuView.as_view(), name='menu'),
]
