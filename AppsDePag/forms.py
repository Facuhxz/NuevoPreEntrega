from django import forms
# from AppsDePag.models import 

# FORMULARIO UTILIZADO PARA ARMAR LA PC
class FormularioPc(forms.Form):
    mother = forms.CharField(max_length=50)
    ram = forms.CharField(max_length=50)
    procesador = forms.CharField(max_length=50)
    placa_de_video = forms.CharField(max_length=50)
    fuente_de_poder = forms.CharField(max_length=50)
    gabinete = forms.CharField(max_length=50)
 
# FORMULARIO PARA PORTATILES
class FormularioPortatiles(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    
    