from django.db import models

# Create your models here.

class Producto(models.Model):
    ProCod = models.CharField(max_length=100)
    ProNom = models.CharField(max_length=100)
    ProCantSto = models.CharField(max_length=100)
    ProNumCodBar = models.CharField(max_length=100)
    ProLinIma = models.CharField(max_length=100)
    ProPreUni = models.CharField(max_length=100)