from django.db import models
# Create your models here.
class Cliente(models.Model):
    CliCode = models.IntegerField()
    CliNom = models.CharField(max_length=100)
    CliEma = models.EmailField()
    CliPas = models.CharField(max_length=100)
    CliNumTel = models.IntegerField()
    CliTipDoc = models.CharField(max_length=100)
    CliNumDoc = models.IntegerField()
    CliFecCum = models.DateField()
    CliHueDig = models.ImageField()
    CliMemCod = models.IntegerField()
    CliMemIni = models.DateField()
    CliMemFin = models.DateField()
class Instructor(models.Model):
    InsCod = models.IntegerField()
    InsNom = models.CharField(max_length=100)
    InsEma = models.EmailField()
    InsPas = models.CharField(max_length=100)
    InsTipDoc = models.IntegerField()
    InsNumDoc = models.IntegerField()
    InsNumTel = models.IntegerField()
    InsFecCum = models.DateField()
    InsHueDig = models.ImageField()
    InsFecIni = models.DateField()

