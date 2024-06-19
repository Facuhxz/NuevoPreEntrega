from django.shortcuts import render, redirect


from AppsDePag.models import PcArmada, PortatilGamer
from AppsDePag.forms import FormularioPc, FormularioPortatiles 


# ESTE CODIGO UTILIZAMOS PARA IR A NUESTRO INICIO
def inicio(request):
    return render(request, "AppsDePag/index.html")

# ESTE CODIGO UTILIZAMOS PARA OBTENER DATOS DE NUESTRA PC
def ArmarPc(request):
    
    formulario = FormularioPc() 
    if request.method == "POST":
        formulario = FormularioPc(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            pc_armada = PcArmada(mother=datos.get("mother"), ram=datos.get("ram"), procesador=datos.get("procesador"),
                                     placa_de_video=datos.get("placa_de_video"), fuente_de_poder=datos.get("fuente_de_poder"),
                                     gabinete=datos.get("gabinete"))
            pc_armada.save()
            return redirect(PcArmadas)
        
     
    return render(request, "AppsDePag/Arma_tu_pc.html", {"formulario": formulario})

# ESTE CODIGO UTILIZAMOS PARA CREAR LA LISTA DE PC ARMADAS
def PcArmadas(request):
    
    PcArmadas = PcArmada.objects.all()
    
    return render(request, "AppsDePag/PcsArmadas.html", {"PcArmadas":PcArmadas})


# ESTE CODIGO UTILIZAMOS PARA OBTENER DATOS DE NUESTRO PORTATIL
def Portatiles(request):
    
    formulario = FormularioPortatiles() 
    if request.method == "POST":
        formulario = FormularioPortatiles(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            portatil_gamer = PortatilGamer(marca=datos.get("marca"), modelo=datos.get("modelo"))
            portatil_gamer.save()
            return redirect(Portatil)
        
                     
    return render(request, "AppsDePag/Portatiles_gamers.html", {"formulario": formulario})

# ESTE CODIGO UTILIZAMOS PARA CREAR LA LISTA DE PORTATILES DISPONIBLES
def Portatil(request):
    
    portatil_gamer = PortatilGamer.objects.all()
    
    return render(request, "AppsDePag/Portatiles.html", {"portatil_gamer":portatil_gamer})        