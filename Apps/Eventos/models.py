from django.db import models

# Create your models here.

class Evento(models.Model):
    EveCod = models.CharField(max_length=100)
    EveNom = models.CharField(max_length=100)
    EveFecDiaHorIni = models.CharField(max_length=100)
    EveFecDiaHorFin = models.CharField(max_length=100)
    EveInsCod = models.CharField(max_length=100)
    EvePre = models.CharField(max_length=100)

class Cliente_Evento(models.Model):
    CliEveCod = models.CharField(max_length=100)
    CliEveCliCod = models.CharField(max_length=100)
    CliEveInsCod = models.CharField(max_length=100)
    CliEveFecDiaHorIni = models.CharField(max_length=100)
    CliEveFecDiaHorIni = models.CharField(max_length=100)
    CliEveFecDiaHorFin = models.CharField(max_length=100)
    CliEveEst = models.CharField(max_length=100)