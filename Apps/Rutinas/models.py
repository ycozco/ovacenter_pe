from django.db import models

# Create your models here.
class Rutina(models.Model):
    RutCod = models.CharField(max_length=100)
    RutNom = models.CharField(max_length=100)
    RutCarPes = models.IntegerField()
    RutNumRep = models.IntegerField()
    RutInsCod = models.CharField(max_length=100)
    RutDes = models.CharField(max_length=100)
class Cliente_Rutina(models.Model):
    CliRutCliCod = models.CharField(max_length=100)
    CliRutInsCod = models.CharField(max_length=100)
    CliRutFecDia = models.DateField()
    CliRutEst = models.BooleanField(default=False)