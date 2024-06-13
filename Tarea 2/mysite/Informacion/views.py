from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import F
from .models import Proyecto, Articulo, Comentario
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
    if request.method == 'POST' :
        Comentario.objects.create(autor = request.POST['nombre'], 
                                contenido = request.POST['cuerpo'], articulo = articulo)
        return HttpResponseRedirect(reverse("Informacion:articulo", args=(id,)))

    comentarios = articulo.comentario_set.order_by("-fecha_publicacion")
    
    return render(request, "Informacion/articulo.html", {
        'articulo' : articulo,
        'form' : HacerComentario(),
        'comentarios' : comentarios,
        'id' : id,
    })

def aumentarLike(request, id):
    articulo = get_object_or_404(Articulo, pk=id)
    articulo.likes = F("likes") + 1
    articulo.save()
    return HttpResponseRedirect(reverse("Informacion:articulo", args=(id,)))