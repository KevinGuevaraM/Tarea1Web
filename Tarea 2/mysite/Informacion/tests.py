from django.test import TestCase
from django.urls import reverse

from .models import Proyecto

# Create your tests here.
def create_proyecto(nombre, descripcion):
    return Proyecto.objects.create(titulo=nombre, descripcion=descripcion)

class ProyectosRecientesTests(TestCase):
    def test_proyecto_no_existente(self):
        response = self.client.get(reverse("Informacion:proyecto", args=(5,)))
        self.assertEqual(response.status_code, 404)

    def test_proyecto_existente(self):
        proyecto = create_proyecto("Hola", "Una descripcion")
        response = self.client.get(reverse("Informacion:proyecto", args=(proyecto.pk,)))
        self.assertEqual(response.status_code, 200)

class VistasBasicasTests(TestCase):
    def test_visita_index(self):
        response = self.client.get(reverse("Informacion:index"))
        self.assertEqual(response.status_code, 200)
    
    def test_visita_resume(self):
        response = self.client.get(reverse("Informacion:resume"))
        self.assertEqual(response.status_code, 200)

    def test_visita_about(self):
        response = self.client.get(reverse("Informacion:about"))
        self.assertEqual(response.status_code, 200)

    def test_visita_enviarMensaje(self):
        response = self.client.get(reverse("Informacion:enviar_mensaje"))
        self.assertEqual(response.status_code, 200)