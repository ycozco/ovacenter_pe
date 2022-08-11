from django.db import models

# Create your models here.
class Rutina(models.Model):
    RutCod = models.CharField(max_length=100)
    RutNom = models.CharField(max_length=100)
    RutCarPes = models.CharField(max_length=100)
    RutNumRep = models.CharField(max_length=100)
    RutInsCod = models.CharField(max_length=100)
    RutDes = models.CharField(max_length=100)
class Cliente_Rutina(models.Model):
    CliRutCliCod = models.CharField(max_length=100)
    CliRutInsCod = models.CharField(max_length=100)
    CliRutFecDia = models.CharField(max_length=100)
    CliRutEst = models.CharField(max_length=100)