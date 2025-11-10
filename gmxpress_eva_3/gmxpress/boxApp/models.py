from django.db import models
from django.utils import timezone
from boxApp.choices import generos
from datetime import datetime
import os

# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre de la Especialidad')
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        db_table = 'especialidad'
        verbose_name ='Especialidad'
        verbose_name_plural = 'Especialidades'

class Area(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=40,verbose_name='Nombre del Área')
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}"
        
    class Meta:
        db_table = 'area'
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

class Empleado(models.Model):
    id = models.CharField(max_length=50, unique=True, primary_key=True, verbose_name='ID del Empleado')
    nombre = models.CharField(max_length=30,verbose_name='Nombre del Empleado')
    paterno = models.CharField(max_length=30,verbose_name='Apellido Paterno del Empleado')
    materno = models.CharField(max_length=30,verbose_name='Apellido Materno del Empleado',blank=True)
    run = models.CharField(max_length=12,verbose_name='RUN')
    genero = models.CharField(max_length=1,choices=generos,default='o')
    cantHoras = models.PositiveIntegerField(default=20,verbose_name='Cantidad de Horas Trabajadas')
    fechaNac = models.DateField(blank=True,null=True,verbose_name='Fecha de Nacimiento del Empleado')
    especialidad = models.ForeignKey(Especialidad,null=False,on_delete=models.RESTRICT)
    area = models.ForeignKey(Area,null=True,on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)

    def generarNombre(instance,filename):
        extension = os.path.splitext(filename)[1][1:]
        ruta = 'empleados'
        fecha = datetime.now().strftime("%d%m%Y_%H%M%S")
        nombre = f"{fecha}.{extension}"
        return os.path.join(ruta,nombre)

    foto = models.ImageField(upload_to=generarNombre,null=True,default='doctores/wntonto.png')



    def __str__(self):
        return f"Emp. {self.nombre} {self.paterno} - {self.especialidad}"

    class Meta:
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['nombre','paterno','materno']

class Producto(models.Model):
    id = models.CharField(max_length=50, unique=True, primary_key=True, verbose_name='ID del Producto')
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Producto')
    stock = models.PositiveIntegerField(verbose_name='Cantidad de Stock')
    hora_ingreso = models.DateField(verbose_name='Fecha de Ingreso')
    precio = models.PositiveIntegerField(verbose_name='Precio')
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
