from django.contrib import admin

from .models import Solicitud , Producto, Pedido
# Register your models here.

admin.site.register(Solicitud)
admin.site.register(Producto)
admin.site.register(Pedido)