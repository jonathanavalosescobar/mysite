from django.urls import path
from . import views 
from .views import info, form, inicio, RegistroUsuario, exito, login_exito, login_salida

from django.contrib import admin
from django.conf.urls import url

from django.contrib.auth.decorators import login_required





urlpatterns = [
    path('', views.post_list, name='al correr django http://127.0.0.1:8000 '),
    path('Armafox', inicio, name='Inicio'),
    path('informacion', info, name='Wiki Armafox'),
    path('RegistroExitoso', exito, name='exito'),
    path('solicitud',login_required(login_exito) , name='redirecion a solicitud cliente'),
    path('logged_out',login_salida , name='redirecion a logout'),
    url(r'form', RegistroUsuario.as_view(), name="redirecion registro exitoso") 
  
]
