from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Descripción', 'Precio', 'Tipo')  # Agregando 'Tipo' a list_display
    search_fields = ('Nombre', 'Descripción')
    list_filter = ('Tipo',)  # Agregar filtro por Tipo
    ordering = ('Nombre',)  # Ordenar alfabéticamente por Nombre
    fields = ('Nombre', 'Precio', 'Descripción', 'Stock', 'Link', 'Tipo')

    actions = ['set_tipo_bebida', 'set_tipo_pan', 'set_tipo_reposteria', 'set_tipo_empanadas']

    def set_tipo(self, request, queryset, tipo):
        queryset.update(Tipo=tipo)

admin.site.register(Producto, ProductoAdmin)
