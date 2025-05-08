from django.contrib import admin
from .models import Producto, Categoria


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'disponible', 'fecha_creacion')
    search_fields = ('nombre',)
    list_filter = ('disponible', 'categoria')  # Filtro por categoría
    list_select_related = ('categoria',)  # Para mejorar el rendimiento al mostrar categorías

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
