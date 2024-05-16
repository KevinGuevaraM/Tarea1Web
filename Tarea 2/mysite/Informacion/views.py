from django.shortcuts import render, get_object_or_404
from .models import Proyecto
from .forms import EnviarMensaje

# Create your views here.

def index(request):
    return render(request, "Informacion/index.html", {
        'proyectos' : Proyecto.objects.all()
    })

def proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    return render(request, "Informacion/proyecto.html", {
        'proyecto' : proyecto
    })

def resume(request):
    return render(request, "Informacion/resume.html")

def about(request):
    return render(request, "Informacion/about.html")

def enviarMensaje(request):
    return render(request, "Informacion/enviarMensaje.html", {
        'form' : EnviarMensaje()
    })