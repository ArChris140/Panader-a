from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Precio = models.IntegerField()
    Descripción = models.CharField(max_length=100)
    Stock = models.IntegerField()
    Link = models.CharField(max_length=255)
    Tipo = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.Nombre} -> {self.Precio}'

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Correo = models.CharField(max_length=30)
    Contraseña = models.CharField(max_length=20)
    Teléfono = models.IntegerField()

class Compra(models.Model):
    id = models.IntegerField(primary_key=True)
    Id_Usuario = models.IntegerField()
    Precio_Total = models.IntegerField()

class Cantidad(models.Model):
    id = models.IntegerField(primary_key=True)
    Id_Producto = models.IntegerField()
    Id_Compra = models.IntegerField()
    Cantidad = models.IntegerField()
    Precio_Cantidad = models.IntegerField()