from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)