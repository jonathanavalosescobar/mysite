from django.shortcuts import render

from django.views.generic import CreateView
from django.contrib.auth.models import User
from app_Armado.forms import RegistroForm
from django.urls import reverse_lazy

# Create your views here.

def post_list(request):
    return render(request, 'plantillas/Armafox.html', {}) # plantilla determinada arranque.

def inicio(request):
    return render(request, 'plantillas/Armafox.html')   # plantilla de inicio.

def info(request):
    return render(request, 'plantillas/informacion.html')  # plantilla de wiki armafox.

def form(request):
    return render(request, 'plantillas/form.html')   # plantilla de registro usuarios.



# para registrar usuario.
class RegistroUsuario(CreateView):
    model = User
    template_name = "plantillas/form.html"
    form_class = RegistroForm
    success_url = reverse_lazy('exito')

# funcion para retornar registro_exitoso.
def exito(request):
    return render(request, 'registration/RegistroExitoso.html')


# funcion para retornar login exitoso dependiendo del tipo de usuario.
def login_exito(request):
    user = request.user
    if user.has_perm('app_Armado.tecnico'):
        
        return render(request, 'plantillas/tecnico.html')   # plantilla con funciones para tecnico.
    else:
        return render(request, 'plantillas/solicitud.html')  # plantilla con funciones para cliente.
    

# funcion para retornar logout.
def login_salida(request):
    return render(request, 'registration/logged_out.html')