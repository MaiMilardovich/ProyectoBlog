from django.db import models

# Create your models here.


class Lugar (models.Model):

    nombre = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)


class Vestidos (models.Model):

    diseñador = models.CharField(max_length=60)
    estilo = models.CharField(max_length=60)


class Proveedores (models.Model):

    proveedor = models.CharField(max_length=60)
    tipo = models.CharField(max_length=20)
    mail = models.EmailField()





