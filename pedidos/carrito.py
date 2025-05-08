# pedidos/carrito.py

from .models import CarritoItem
from productos.models import Producto
from django.shortcuts import get_object_or_404

class CarritoDB:
    def __init__(self, request):
        self.user = request.user

    def agregar(self, producto_id):
        producto = get_object_or_404(Producto, id=producto_id)
        item, creado = CarritoItem.objects.get_or_create(
            usuario=self.user,
            producto=producto,
            defaults={'cantidad': 1}
        )
        if not creado:
            item.cantidad += 1
            item.save()

    def eliminar(self, producto_id):
        producto = get_object_or_404(Producto, id=producto_id)
        CarritoItem.objects.filter(usuario=self.user, producto=producto).delete()

    def limpiar(self):
        CarritoItem.objects.filter(usuario=self.user).delete()

    def obtener_items(self):
        return CarritoItem.objects.filter(usuario=self.user)

    def total(self):
        return sum(item.subtotal() for item in self.obtener_items())
