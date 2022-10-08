from django.db import models
import datetime
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.


class Lugar (models.Model):

    nombre = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)


class Vestidos (models.Model):

    autor=models.CharField(max_length=40, default="")
    diseñador = models.CharField(max_length=60)
    estilo = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to="vestidos", null=True, blank=True)
    fechaCarga = models.DateField(default = timezone.now())


class Proveedores (models.Model):

    proveedor = models.CharField(max_length=60)
    tipo = models.CharField(max_length=20)
    mail = models.EmailField()





