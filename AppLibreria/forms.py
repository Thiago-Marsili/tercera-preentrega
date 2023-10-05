from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    
class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    cargo = forms.CharField(max_length=30)

class LibroForm(forms.Form):
    nombrel = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)