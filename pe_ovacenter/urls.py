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

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from Apps.Users.views import ClienteViewSet,InstructorViewSet
from Apps.Eventos.views import EventosViewSet
from inicio.views import Inicio

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'instructor', InstructorViewSet)
router.register(r'eventos', EventosViewSet)

urlpatterns = [
    path('datos' ,Inicio, name = "inicio"),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('ovagym/', include('ovagym.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
