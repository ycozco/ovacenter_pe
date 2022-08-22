
from django.contrib import admin
from .models import Membresia, Venta ,Gastos
# Register your models here.

admin.site.register(Venta)
admin.site.register(Membresia)
admin.site.register(Gastos)
