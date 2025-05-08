from django.shortcuts import render, redirect
from .models import Producto, Categoria
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required


def catalogo(request):
    categoria_id = request.GET.get('categoria')  # Obtener el parámetro 'categoria' de la URL
    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id)
    else:
        productos = Producto.objects.all()

    categorias = Categoria.objects.all()  # Obtener todas las categorías para mostrarlas en el filtro

    return render(request, 'productos/catalogo.html', {'productos': productos, 'categorias': categorias})

