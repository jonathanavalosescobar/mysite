from django.shortcuts import render

from .models import Solicitud, Producto, Pedido

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
        
        pedi = Pedido.objects.all()

        if request.POST:

            idped = request.POST.get("id_pedido", "")
            codpro = request.POST.get("codigo_producto", "")
            rutcli = request.POST.get("rut_cliente", "")
            nomcli = request.POST.get("nombre_cliente", "")
            rutvisi = request.POST.get("rut_visitante", "")
            nomvisi = request.POST.get("nombre_visitante", "")
            estpe = request.POST.get("estado_pedido", "")
            numcel = request.POST.get("numero_celular", "")
            fechdes = request.POST.get("fecha_de_despacho", "")
        
            pedi = Pedido(
                id_pedido=idped,
                codigo_producto = codpro,
                rut_cliente=rutcli,
                nombre_cliente=nomcli,
                rut_visitante=rutvisi,
                nombre_visitante=nomvisi,
                estado_pedido=estpe,
                numero_celular=numcel,
                fecha_de_despacho=fechdes
            )
            pedi.save()
        return render(request, 'plantillas/tecnico.html')   # plantilla con funciones para tecnico.

    else:
        soli = Solicitud.objects.all()
       

        if request.POST:

            idser = request.POST.get("id_servicio", "")
            rut = request.POST.get("rut_cliente", "")
            nomcomp = request.POST.get("Nombre_completo", "")
            fechvi = request.POST.get("fecha_de_visita", "")
            horavi = request.POST.get("hora_de_visita", "")
            dire = request.POST.get("direccion", "")
            presu = request.POST.get("preosupuesto", "")
            descrip = request.POST.get("descripcion_pc_a_solicitar", "")
            desea = request.POST.get("desea_induccion", "")
            num = request.POST.get("numero_celular", "")
    
            
            soli = Solicitud(
                id_servicio=idser,
                rut_cliente=rut,
                Nombre_completo=nomcomp,
                fecha_de_visita=fechvi,
                hora_de_visita=horavi,
                direccion=dire,
                preosupuesto=presu,
                descripcion_pc_a_solicitar=descrip,
                desea_induccion=desea,
                numero_celular=num,
            )
            soli.save()
        return render(request, 'plantillas/solicitud.html')  # plantilla con funciones para cliente.
    



# funcion para retornar logout.
def login_salida(request):
    return render(request, 'registration/logged_out.html')

def listar_solicitud(request):
    soli= Solicitud.objects.all()
    return render(request, 'plantillas/solicitud.html', {'solicitud': soli})

def lista_solicitudestecnico(request):
    soli = Solicitud.objects.all()
    return render(request, 'plantillas/tecnico.html', {'solicitud': soli})

def listarproductos(request):
    prod = Producto.objects.all()
    return render(request, 'plantillas/tecnico.html', {'productos': prod})