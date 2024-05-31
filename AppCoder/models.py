from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    emal = models.EmailField(null=True)

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    emal = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechadeentrega = models.DateField()
    entregado = models.BooleanField()
