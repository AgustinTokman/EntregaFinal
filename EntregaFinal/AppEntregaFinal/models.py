from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()
    
class Tienda(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)   
    