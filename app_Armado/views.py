from django.shortcuts import render



# Create your views here.

def post_list(request):
    return render(request, 'plantillas/Armafox.html', {})

def inicio(request):
    return render(request, 'plantillas/Armafox.html')   

def info(request):
    return render(request, 'plantillas/informacion.html')  

def form(request):
    return render(request, 'plantillas/form.html')   








