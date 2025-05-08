from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre de la categoría: Galletas, Pasteles, Postres

    def __str__(self):
        return self.nombre
class Producto(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del producto
    descripcion = models.TextField()  # Descripción detallada
    precio = models.DecimalField(max_digits=7, decimal_places=2)  # Precio del producto
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  # Imagen opcional
    disponible = models.BooleanField(default=True)  # Si está disponible para compra
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha en que se creó
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.SET_NULL, null=True, blank=True) # Relación con la categoría
    def __str__(self):
        return self.nombre