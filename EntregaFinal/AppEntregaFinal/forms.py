from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    telefono = forms.IntegerField()

class TiendaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    telefono = forms.IntegerField()
    

class CategoriaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=40)      
            