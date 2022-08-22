from django.db import models

# Create your models here.

class Evento(models.Model):
    EveCod = models.CharField(max_length=100)
    EveNom = models.CharField(max_length=100)
    EveFecDiaHorIni = models.DateField()
    EveFecDiaHorFin = models.DateField()
    EveInsCod = models.CharField(max_length=100)
    EvePre = models.DecimalField(max_digits=2, decimal_places=2)

class Cliente_Evento(models.Model):
    CliEveCod = models.CharField(max_length=100)
    CliEveCliCod = models.CharField(max_length=100)
    CliEveInsCod = models.CharField(max_length=100)
    CliEveFecDiaHorIni = models.DateField()
    CliEveFecDiaHorIni = models.DateField()
    CliEveFecDiaHorFin = models.DateField()
    CliEveEst = models.BooleanField(default=False)