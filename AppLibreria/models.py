from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    cargo = models.CharField(max_length=30)

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)


class Libro(models.Model):
    nombrel = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)