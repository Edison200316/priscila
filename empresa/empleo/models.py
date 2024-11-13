from django.db import models

# Create your models here.
class Empleado(models.Model):
    id = models.AutoField(max_length=100,blank=False,primary_key=True)
    nombre = models.CharField(max_length=100,blank=False)
    apellido = models.CharField(max_length=100,blank=False)
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()
    fecha_despido = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nombre
