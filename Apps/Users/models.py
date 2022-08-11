from django.db import models
from rest_framework import serializers
# Create your models here.

class Cliente(models.Model):
    CliCode = models.CharField(max_length=100)
    CliNom = models.CharField(max_length=100)
    CliEma = models.CharField(max_length=100)
    CliPas = models.CharField(max_length=100)
    CliNumTel = models.CharField(max_length=100)
    CliTipDoc = models.CharField(max_length=100)
    CliNumDoc = models.CharField(max_length=100)
    CliFecCum = models.CharField(max_length=100)
    CliHueDig = models.CharField(max_length=100)
    CliMemCod = models.CharField(max_length=100)
    CliMemIni = models.CharField(max_length=100)
    CliMemFin = models.CharField(max_length=100)

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['CliNom', 'CliEma']
class Instructor(models.Model):
    InsCod = models.CharField(max_length=100)
    InsNom = models.CharField(max_length=100)
    InsEma = models.CharField(max_length=100)
    InsPas = models.CharField(max_length=100)
    InsTipDoc = models.CharField(max_length=100)
    InsNumDoc = models.CharField(max_length=100)
    InsNumTel = models.CharField(max_length=100)
    InsFecCum = models.CharField(max_length=100)
    InsHueDig = models.CharField(max_length=100)
    InsFecIni = models.CharField(max_length=100)
