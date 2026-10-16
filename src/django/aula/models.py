from django.db import models

# Create your models here.

class Person(models.Model):
    first_name =models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age =models.IntegerField(null=True, blank=True)
    
class Musico(models.Model):
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    instrumento = models.CharField(max_length=100)
    
class Album(models.Model):
    artista =models.ForeignKey(Musico, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_salida =models.DateField()
    estrellas = models.IntegerField()
    
# ejemplo
class Autor(models.Model):
    nombre =models.CharField(max_length=100)
    apellido =models.CharField(max_length=100)
    
class Libro(models.Model):
    autor =models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo =models.CharField(max_length=100)
    anio =models.IntegerField()
    
class Lector(models.Model):
    nombre =models.CharField(max_length=100)
    apellido =models.CharField(max_length=100)
    email =models.CharField(max_length=50)
