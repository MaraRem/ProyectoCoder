from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} - {self.camada}'
    
    class Meta():
        unique_together = ('nombre','camada')



class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    emal = models.EmailField(null=True)
    
    def __str__(self):
        return f'{self.nombre} - {self.apellido} '
    
    class Meta():
        unique_together = ('nombre','apellido')


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    emal = models.EmailField()
    profesion = models.CharField(max_length=30)

    
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.profesion}'

    class Meta():
        unique_together = ('nombre','apellido')


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechadeentrega = models.DateField()
    entregado = models.BooleanField()
    

    def __str__(self):
        return f'{self.nombre} - {self.entregado} - {self.fechadeentrega}'