from django.db import models

# Create your models here.

class Alumno (models.Model):
    apaterno=models.CharField(max_length=50, verbose_name='Apellido Paterno')
    amaterno=models.CharField(max_length=50, verbose_name='Apellido Materno')
    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    fechas_nacimiento= models.DateField(verbose_name='Fecha de nacimiento'), null=False, blank=False
    fechas_nacimiento= models.DateField(verbose_name='Fecha de ingleso'), null=False, blank=False