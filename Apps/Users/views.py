from django.shortcuts import render
from django.core import serializers
from rest_framework import viewsets
from .models import ClienteSerializer,Cliente,Instructor,InstructorSerializer
from django.http import HttpResponse
# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class =InstructorSerializer