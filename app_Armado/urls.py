from django.urls import path
from . import views 
from .views import info,form,inicio






urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', inicio, name='Armafox'),
    path('informacion', info, name='informacion'),
    path('form', form, name='form'),
  
]
