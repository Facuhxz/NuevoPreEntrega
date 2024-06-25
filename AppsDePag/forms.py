from django import forms
# from AppsDePag.models import 

# FORMULARIO UTILIZADO PARA ARMAR LA PC
class FormularioPcBase(forms.Form):
    pc = forms.CharField(max_length=50)
    mother = forms.CharField(max_length=50)
    ram = forms.CharField(max_length=50)
    procesador = forms.CharField(max_length=50)
    placa_de_video = forms.CharField(max_length=50)
    fuente_de_poder = forms.CharField(max_length=50)
    gabinete = forms.CharField(max_length=50)
    
class FormularioPc(FormularioPcBase):
    ...
    
class EditarPc(FormularioPcBase):
    ...
    
 
class BuscarPc(forms.Form):
    pc = forms.CharField(max_length=50, required=False)    
    