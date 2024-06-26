from django.urls import path

from . import views

app_name = "Informacion"
urlpatterns = [
    path("", views.index, name="index"),
    path("proyecto/<int:id>", views.proyecto, name="proyecto"),
    path("resume", views.resume, name="resume"),
    path("about", views.about, name="about"),
    path("enviar_mensaje", views.enviarMensaje, name="enviar_mensaje"),
    path("blog", views.blog, name="blog"),
    path("articulo/<int:id>", views.articulo, name="articulo"),
    path("cambioOrden", views.cambioOrden, name="cambioOrden"),
    path("articulo/<int:id>/like", views.aumentarLike, name="aumentarLike"),
    path("logout", views.logout_view, name="logout"),
]