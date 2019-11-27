from django.contrib.auth.models import User
from app_Armado.models import Producto
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url', 'id_producto', 'procesador' , 'placa' , 'memoria_ram' , 'tarjeta_video' , 'disco_duro', 'modelo_gabinete', 'precio')
