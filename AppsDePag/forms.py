from django import forms
# from AppsDePag.models import 

class FormularioPc(forms.Form):
    mother = forms.CharField(max_length=50)
    ram = forms.CharField(max_length=50)
    procesador = forms.CharField(max_length=50)
    placa_de_video = forms.CharField(max_length=50)
    fuente_de_poder = forms.CharField(max_length=50)
    gabinete = forms.CharField(max_length=50)
    
   
        
    
    # def __str__(self):
    #    return f"Armaste tu pc {self.mother} {self.ram} {self.procesador} {self.placa_de_video} {self.fuente_de_poder} {self.gabinete}"


    
    