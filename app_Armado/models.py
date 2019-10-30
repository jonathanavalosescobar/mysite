from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Solicitud(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    rut_cliente= models.CharField(max_length=12)
    Nombre_completo = models.CharField(max_length=100)
    fecha_de_visita = models.DateField()
    hora_de_visita = models.CharField(max_length=5)
    direccion= models.CharField(max_length=100)   
    preosupuesto = models.CharField(max_length=7)
    descripcion_pc_a_solicitar= models.CharField(max_length=50)       
    desea_induccion= models.CharField(max_length=2)  
    numero_celular = models.CharField(max_length=8)
  
    def __str__(self):
        return self.rut_cliente

    
    class Meta:
        permissions = (
            ('tecnico',_('Es tecnico')),
        )