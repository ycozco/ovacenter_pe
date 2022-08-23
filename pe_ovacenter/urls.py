"""pe_ovacenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from rest_framework import routers 
from api.views import EventosViewSet,ClienteViewSet,InstructorViewSet
from inicio.views import Inicio
from rest_framework.urlpatterns import format_suffix_patterns
from Apps.Users.views import ClienteShowObject
from api.views import Cliente_list,Cliente_detail
from Apps.Users.views import UserCreateView
router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'instructor', InstructorViewSet)
router.register(r'eventos', EventosViewSet)

urlpatterns = [
    path('' ,Inicio, name = "inicio"),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('ovagym/', include('ovagym.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/',Cliente_list,name='browsing'),
    path('users/<int:pk>',Cliente_detail,name='browsing'),
    path('inscription/',UserCreateView,name='inscription'),

]

