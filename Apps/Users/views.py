from django.shortcuts import render
from django.core import serializers
from rest_framework import viewsets
from .models import ClienteSerializer,Cliente
from django.http import HttpResponse
# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer