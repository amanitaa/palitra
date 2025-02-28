"""
URL configuration for palitra_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from filebrowser.sites import site

from palitra_blog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/filebrowser/', site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('api/comments/', include('comments.urls', namespace='comments')),
    path('api/users/', include('user.urls', namespace='users')),
    path('api/tags/', include('tags.urls', namespace='tags')),
    path('api/menu/', include('menu.urls', namespace='menu')),
    path('api/categories/', include('categories.urls', namespace='categories')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
