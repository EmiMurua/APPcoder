from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre= models.CharField(max_length=40)
    camada = models.IntegerField()

class estudiante(models.Model):

    nombre= models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)

