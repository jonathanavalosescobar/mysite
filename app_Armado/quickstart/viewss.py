
from django.contrib.auth.models import User
from app_Armado.models import Producto
from rest_framework import viewsets
from app_Armado.quickstart.serializers import UserSerializer, ProductoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Userpermissions to be viewed or edited.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer