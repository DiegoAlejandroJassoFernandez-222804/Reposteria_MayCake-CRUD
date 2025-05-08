# admin/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from productos.models import Producto
from productos.forms import ProductoForm, CategoriaForm
from pedidos.models import Pedido
from django.contrib.auth.models import User
from django.db.models import Q

def inicio_maycake(request):
    return render(request, 'inicio.html')

@staff_member_required
def panel_principal(request):
    return render(request, 'adminpanel/index.html')

@staff_member_required
def lista_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-fecha')
    return render(request, 'adminpanel/lista_pedidos.html', {'pedidos': pedidos})

@staff_member_required
def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    detalles = pedido.detalles.all()

    if request.method == 'POST':
        nuevo_estado = request.POST.get('nuevo_estado')
        if nuevo_estado in ['pendiente', 'listo', 'entregado']:
            pedido.estado = nuevo_estado
            pedido.save()

    return render(request, 'adminpanel/detalle_pedido.html', {'pedido': pedido, 'detalles': detalles})

@staff_member_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminpanel:agregar_producto')  # O donde quieras redirigir
    else:
        form = CategoriaForm()
    return render(request, 'adminpanel/crear_categoria.html', {'form': form})

@staff_member_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminpanel:lista_productos')  # redirige al catálogo después de guardar
    else:
        form = ProductoForm()
    return render(request, 'adminpanel/agregar_producto.html', {'form': form})

@staff_member_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('adminpanel:lista_productos')  # Cambia según tu ruta
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'adminpanel/editar_producto.html', {'form': form, 'producto': producto})

@staff_member_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('adminpanel:lista_productos')
    return render(request, 'adminpanel/eliminar_producto.html', {'producto': producto})

@staff_member_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'adminpanel/lista_productos.html', {'productos': productos})


@staff_member_required
def gestionar_usuarios(request):
    query = request.GET.get('q')
    if query:
        usuarios = User.objects.filter(
            Q(username__icontains=query) |
            Q(email__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )
    else:
        usuarios = User.objects.all()
    return render(request, 'adminpanel/gestionar_usuarios.html', {'usuarios': usuarios})

@staff_member_required
def dar_de_baja_usuario(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    usuario.is_active = False
    usuario.save()
    return redirect('adminpanel:gestionar_usuarios')

@staff_member_required
def reactivar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    usuario.is_active = True
    usuario.save()
    return redirect('adminpanel:gestionar_usuarios')
