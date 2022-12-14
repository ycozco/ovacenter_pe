from django.db import models

# Create your models here.

class Venta(models.Model):
    VenCod = models.CharField(max_length=100)
    VenProCod = models.CharField(max_length=100)
    VenCliCod = models.CharField(max_length=100)
    VenForPagCod = models.CharField(max_length=100)
    VenFec = models.CharField(max_length=100)

class Membresia(models.Model):
    MemCod = models.CharField(max_length=100)
    MemNom = models.CharField(max_length=100)
    MemDes = models.CharField(max_length=100)
    MemCanMes = models.CharField(max_length=100)
    MemPre = models.CharField(max_length=100)

class Gastos(models.Model):
    GasCod = models.CharField(max_length=100)
    GasNom = models.CharField(max_length=100)
    GasForPagCod = models.CharField(max_length=100)
    GasDes = models.CharField(max_length=100)
    GasFec = models.CharField(max_length=100)
