from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=5000)
    fecha_publicacion = models.DateTimeField(auto_now=True)
    likes = models.IntegerField()

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=2000)
    autor = models.CharField(max_length=500)
    fecha_publicacion = models.DateTimeField(auto_now=True)