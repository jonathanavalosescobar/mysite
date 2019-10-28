from django.urls import path
from . import views 
from .views import info, form, inicio, RegistroUsuario, exito, login_exito, login_salida

from django.contrib import admin
from django.conf.urls import url

from django.contrib.auth.decorators import login_required





urlpatterns = [
    path('', views.post_list, name='post_list '),
    path('Armafox', inicio, name='Armafox'),
    path('informacion', info, name='ingormacion'),
    path('RegistroExitoso', exito, name='exito'),
    path('solicitud',login_required(login_exito) , name='solicitud'),
    path('logged_out',login_salida , name='logged_out'),
    url(r'form', RegistroUsuario.as_view(), name="form") 
  
]
