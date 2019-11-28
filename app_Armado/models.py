from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Solicitud(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    rut_cliente= models.CharField(max_length=12)
    Nombre_completo = models.CharField(max_length=100)
    fecha_de_visita = models.CharField(max_length=10)
    hora_de_visita = models.CharField(max_length=5)
    direccion= models.CharField(max_length=100)   
    preosupuesto = models.CharField(max_length=9)
    descripcion_pc_a_solicitar= models.CharField(max_length=50)       
    desea_induccion= models.CharField(max_length=2)  
    numero_celular = models.CharField(max_length=8)

    def __str__(self):
        return self.rut_cliente


# Modelo para llenar de admin y listar en tecnico
class Producto(models.Model):
    
    id_producto= models.TextField(max_length=12,primary_key=True)
    procesador = models.TextField(max_length=22)
    placa  = models.TextField(max_length=22)
    memoria_ram= models.TextField(max_length=22)
    tarjeta_video= models.TextField(max_length=22)
    disco_duro = models.TextField(max_length=22)
    modelo_gabinete  = models.TextField(max_length=20)
    precio = models.TextField(max_length=20)
    imagen = models.ImageField(upload_to="Productos",null=True)
    
    def __str__(self):
        return self.procesador
  

# Modelo para generar pedido de tecnico
class Pedido(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    codigo_producto = models.CharField(max_length=4)
    rut_cliente= models.CharField(max_length=12)
    nombre_cliente = models.CharField(max_length=50)
    rut_visitante= models.CharField(max_length=12)
    nombre_visitante = models.CharField(max_length=100)
    estado_pedido= models.CharField(max_length=2)
    numero_celular = models.CharField(max_length=8)
    fecha_de_despacho = models.CharField(max_length=10)

    def __str__(self):
        return self.rut_cliente

    class Meta:
        permissions = (
            ('tecnico',_('Es tecnico')),
        )
