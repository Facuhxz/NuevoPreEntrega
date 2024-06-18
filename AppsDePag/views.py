from django.shortcuts import render, redirect


from AppsDePag.models import PcArmada
from AppsDePag.forms import FormularioPc


# ESTE CODIGO UTILIZAMOS PARA IR A NUESTRO INICIO
def inicio(request):
    return render(request, "AppsDePag/index.html")

# ESTE CODIGO UTILIZAMOS PARA ARMAR NUESTRA PC
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
