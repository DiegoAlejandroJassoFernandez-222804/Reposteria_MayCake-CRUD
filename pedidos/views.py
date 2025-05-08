# pedidos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from productos.models import Producto
from .models import Pedido, DetallePedido, CarritoItem
from django.contrib import messages
from .forms import MetodoPagoForm


@login_required
def ver_carrito(request):
    items = CarritoItem.objects.filter(usuario=request.user)
    total = sum(item.producto.precio * item.cantidad for item in items)

    return render(request, "pedidos/carrito.html", {
        "items": items,
        "total": round(total, 2)
    })

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    item, creado = CarritoItem.objects.get_or_create(usuario=request.user, producto=producto)

    if not creado:
        item.cantidad += 1
        item.save()

    messages.success(request, f"Se agregó {producto.nombre} al carrito.")
    return redirect("ver_carrito")

@login_required
def eliminar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    CarritoItem.objects.filter(usuario=request.user, producto=producto).delete()
    messages.info(request, f"Se eliminó {producto.nombre} del carrito.")
    return redirect("ver_carrito")

@login_required
def aumentar_cantidad(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    item, creado = CarritoItem.objects.get_or_create(
        usuario=request.user, 
        producto=producto
    )
    item.cantidad += 1
    item.save()
    messages.success(request, f"Se aumentó la cantidad de {producto.nombre}.")
    return redirect("ver_carrito")

@login_required
def disminuir_cantidad(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    try:
        item = CarritoItem.objects.get(
            usuario=request.user, 
            producto=producto
        )
        if item.cantidad > 1:
            item.cantidad -= 1
            item.save()
            messages.info(request, f"Se redujo la cantidad de {producto.nombre}.")
        else:
            item.delete()
            messages.info(request, f"Se eliminó {producto.nombre} del carrito.")
    except CarritoItem.DoesNotExist:
        messages.error(request, "Este producto no está en tu carrito.")
    return redirect("ver_carrito")

@login_required
def procesar_pedido(request):
    carrito = CarritoItem.objects.filter(usuario=request.user)

    if not carrito.exists():
        return redirect("ver_carrito")

    if request.method == "POST":
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            metodo = form.cleaned_data["metodo"]
            pedido = Pedido.objects.create(usuario=request.user, metodo_pago=metodo)

            for item in carrito:
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=item.producto,
                    cantidad=item.cantidad,
                    subtotal=item.producto.precio * item.cantidad,
                )

            carrito.delete()
            return render(request, "pedidos/mis_pedidos.html", {"pedido": pedido})
    else:
        form = MetodoPagoForm()

    return render(request, "pedidos/procesar_pedido.html", {
        "items": carrito,
        "total": sum(item.producto.precio * item.cantidad for item in carrito),
        "form": form,
    })

@login_required
def mis_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-fecha')
    from django.db.models import Sum
    pedidos = pedidos.annotate(total=Sum('detalles__subtotal'))
    pedidos_enumerados = list(enumerate(pedidos, start=1))
    return render(request, 'pedidos/mis_pedidos.html', {'pedidos_enumerados': pedidos_enumerados})

@login_required
def detalle_mi_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, usuario=request.user)
    detalles = pedido.detalles.all()
    # Obtener todos los pedidos del usuario ordenados por fecha
    pedidos_usuario = Pedido.objects.filter(usuario=request.user).order_by('fecha')
    
    # Obtener el número relativo del pedido actual
    numero_pedido = list(pedidos_usuario).index(pedido) + 1
    
    return render(request, 'pedidos/detalle_mi_pedido.html', {
        'pedido': pedido,
        'detalles': detalles,
        'numero_pedido': numero_pedido,
        
    })