from django import forms

class EnviarMensaje(forms.Form):
    #Correo
    correo = forms.EmailField(label="Correo")
    #Nombre
    nombre = forms.CharField(label="Nombre", max_length=150)
    #Cuerpo
    cuerpo = forms.CharField(widget=forms.Textarea)

class HacerComentario(forms.Form):
    #nombre
    nombre = forms.CharField(label="Nombre", max_length=150)
    #Cuerpo
    cuerpo = forms.CharField(widget=forms.Textarea)