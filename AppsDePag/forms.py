from django import forms 

class FormularioMother(forms.Form):
    marca = forms.CharField(max_length=10)
    modelo = forms.CharField(max_length=10)
    
    