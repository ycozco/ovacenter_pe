from django.db import models

# Create your models here.

class Producto(models.Model):
    ProCod = models.CharField(max_length=100)
    ProNom = models.CharField(max_length=100)
    ProCantSto = models.IntegerField()
    ProNumCodBar = models.IntegerField()
    ProLinIma = models.CharField(max_length=100)
    ProPreUni = models.DecimalField(decimal_places=1,max_digits=2)