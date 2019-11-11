from django.urls import path
from . import views 
from .views import info, form, inicio, RegistroUsuario, exito, login_exito, login_salida, listar_solicitud, listarproductos, listarpedidos, listar_solicitud_tecnico

from django.contrib import admin
from django.conf.urls import url

from django.contrib.auth.decorators import login_required





urlpatterns = [
    path('', views.post_list, name='post_list '),
    path('Armafox', inicio, name='Armafox'),
    path('informacion', info, name='informacion'),
    path('RegistroExitoso', exito, name='exito'),
    
    path('solicitud',login_required(login_exito) , name='solicitud'),
    path('tecnico',login_required(login_exito) , name='tecnico'),
   
    path('listar_solicitud',login_required(listar_solicitud) , name='listar_solicitud'),
    path('listar_soli_tecnico',login_required(listar_solicitud_tecnico) , name='listar_soli_tecnico'),

    path('listar_producto',login_required(listarproductos),name="listar_producto"),
    path('listar_pedidos',login_required(listarpedidos),name="listarpedidos"),

    path('logged_out',login_salida , name='logged_out'),
    url(r'form', RegistroUsuario.as_view(), name="form") 
  
]
