from django.urls import path, include
from . import views

app_name = 'adminpanel'

urlpatterns = [
    path('', views.panel_principal, name='panel_principal'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('usuarios/', views.gestionar_usuarios, name='gestionar_usuarios'),
    path('usuarios/dar_de_baja/<int:usuario_id>/', views.dar_de_baja_usuario, name='dar_de_baja_usuario'),
    path('usuarios/reactivar/<int:usuario_id>/', views.reactivar_usuario, name='reactivar_usuario'),
    path('categorias/agregar/', views.crear_categoria, name='crear_categoria'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:producto_id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/', views.lista_productos, name='lista_productos'),  # Nueva ruta para listar productos
]
