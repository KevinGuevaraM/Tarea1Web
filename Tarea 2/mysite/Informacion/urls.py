from django.urls import path

from . import views

app_name = "Informacion"
urlpatterns = [
    path("", views.index, name="index"),
    path("proyecto/<int:id>", views.proyecto, name="proyecto"),
    path("resume", views.resume, name="resume"),
    path("about", views.about, name="about"),
    path("enviar_mensaje", views.enviarMensaje, name="enviar_mensaje"),
]