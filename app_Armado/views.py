from django.shortcuts import render

from django.views.generic import CreateView
from django.contrib.auth.models import User
from app_Armado.forms import RegistroForm
from django.urls import reverse_lazy

# Create your views here.

def post_list(request):
    return render(request, 'plantillas/Armafox.html', {})

def inicio(request):
    return render(request, 'plantillas/Armafox.html')   

def info(request):
    return render(request, 'plantillas/informacion.html')  

def form(request):
    return render(request, 'plantillas/form.html')   



# para registrar usuario.
class RegistroUsuario(CreateView):
    model = User
    template_name = "plantillas/form.html"
    form_class = RegistroForm
    success_url = reverse_lazy('exito')

# funcion para retornar registro_exitoso.
def exito(request):
    return render(request, 'plantillas/RegistroExitoso.html')


# funcion para retornar login_exitoso.
def login_exito(request):
    return render(request, 'plantillas/solicitud.html')

# funcion para retornar logout.
def login_salida(request):
    return render(request, 'registration/logged_out.html')