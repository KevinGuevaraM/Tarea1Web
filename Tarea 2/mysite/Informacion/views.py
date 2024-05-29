from django.shortcuts import render, get_object_or_404
from .models import Proyecto, Articulo
from .forms import EnviarMensaje, HacerComentario

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

def blog(request):
    articulos = Articulo.objects.all()
    return render(request, "Informacion/blog.html", {
        'articulos' : articulos,
        'cantidad' : 5,
        'orden' : "Relevantes",
    })

def cambioOrden(request):
    articulos = Articulo.objects.all()
    try:
        cantidad = request.POST["cantidad"]
        orden = request.POST["orden"]
    except:
        return render("Informacion/index.html")
    else:
        return render(request, "Informacion/blog.html", {
        'articulos' : articulos,
        'cantidad' : cantidad,
        'orden' : orden,
    })

def articulo(request, id):
    articulo = get_object_or_404(Articulo, pk=id)
    return render(request, "Informacion/articulo.html", {
        'articulo' : articulo,
        'form' : HacerComentario(),
    })

def hacerComentario(request):
    return render(request, "Informacion/index.html")