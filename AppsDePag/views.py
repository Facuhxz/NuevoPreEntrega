from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
import random
from AppsDePag.models import MotherBoard
from AppsDePag.forms import FormularioMother



def inicio(request):
    # return HttpResponse("Bienvenidos a mi INICIO!")
    
    # return render(request, "AppsDePag/index.html")
    return render(request, "Padre.html")


def template4(request, nombre, apellido, edad):
      
    
    fecha = datetime.now()
    
    datos = {
            "fecha":fecha,
             "nombre":nombre,
             "apellido":apellido,
             "edad":edad,
             }
    
    
    return render(request,"template.html", datos)

def probando(request):
    
    lista = list(range(500))
       
    numeros = random.choices(lista, k=50)
    
    print(numeros)
       
    return render(request, "If_for.html", {"numeros": numeros})

def creacion_de_mother(request, modelo, marca):
    
    mother = MotherBoard(modelo=modelo, marca=marca)
    
    mother.save()
    
    return render(request, "mothers.template/crear_mother.html", {"mother": mother})

def creacion_de_mother_v2(request):
    
    # v1
    # if request.method == "POST":
    #     mother = MotherBoard(modelo=request.POST.get("Modelo"), marca=request.POST.get("Marca"))
    #     mother.save()
    
    # return render(request, "AppsDePag/crear_mother_v2.html")
    
    
    # v2
    if request.method == "POST":
        
        ...
        # mother = MotherBoard(modelo=request.POST.get("Modelo"), marca=request.POST.get("Marca"))
        # mother.save()
    
    formulario = FormularioMother()    
    
    return render(request, "AppsDePag/crear_mother_v2.html", {"formulario": formulario})
