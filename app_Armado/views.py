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


# funcion para retornar login exitoso dependiendo del tipo de usuario.
def login_exito(request):
    user = request.user
    if user.has_perm('app_Armado.tecnico'):
        
        return render(request, 'plantillas/tecnico.html')
    else:
        return render(request, 'plantillas/solicitud.html')  
    

# funcion para retornar logout.
def login_salida(request):
    return render(request, 'plantillas/logged_out.html')