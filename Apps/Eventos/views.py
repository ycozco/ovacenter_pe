from django.shortcuts import render
from .models import EventoSerializer,Evento
from rest_framework import viewsets
from datetime import datetime

# Create your views here.
class EventosViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer



