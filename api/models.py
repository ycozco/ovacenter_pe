from django.db import models
from rest_framework import serializers
from Apps.Eventos.models import Evento 
from Apps.Users.models import Cliente, Instructor
# Create your models here.

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ['EveCod','EveNom','EveFecDiaHorIni','EveFecDiaHorFin','EveInsCod','EvePre',]

class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instructor
        fields = ['InsCod','InsNom','InsEma','InsPas'] 

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['CliCode','CliNom', 'CliEma', 'CliPas', 'CliNumTel','CliNumDoc','CliFecCum']