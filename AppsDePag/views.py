from django.shortcuts import render, redirect


from AppsDePag.models import PcArmada
from AppsDePag.forms import FormularioPc, BuscarPc, EditarPc


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
            pc_armada = PcArmada(pc=datos.get("pc"), mother=datos.get("mother"), ram=datos.get("ram"), procesador=datos.get("procesador"),
                                     placa_de_video=datos.get("placa_de_video"), fuente_de_poder=datos.get("fuente_de_poder"),
                                     gabinete=datos.get("gabinete"))
            pc_armada.save()
            return redirect(PcArmadas)
        
     
    return render(request, "AppsDePag/Arma_tu_pc.html", {"formulario": formulario})

# ESTE CODIGO UTILIZAMOS PARA CREAR LA LISTA DE PC ARMADAS
def PcArmadas(request):
    formulario = BuscarPc(request.GET)
    if formulario.is_valid():
        pc = formulario.cleaned_data["pc"]
        PcArmadas = PcArmada.objects.filter(pc=pc)
    
    # PcArmadas = PcArmada.objects.all()
    
    return render(request, "AppsDePag/PcsArmadas.html", {"PcArmadas": PcArmadas, "formulario": formulario})

def EliminarPc(request, id):
    pc = PcArmada.objects.get(id=id)
    pc.delete()
    
    return redirect(PcArmadas)

def EditarPC(request, id):
    pc = PcArmada.objects.get(id=id)
    formulario = EditarPc(initial={"pc": pc.pc, "mother": pc.mother, "ram": pc.ram, "procesador": pc.procesador,
                                   "placa_de_video": pc.placa_de_video, "fuente_de_poder": pc.fuente_de_poder,
                                   "gabinete": pc.gabinete})
    
    if request.method == "POST":
        formulario = EditarPc(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            pc.pc = info["pc"]
            pc.mother = info["mother"]
            pc.ram = info["ram"]
            pc.procesador = info["procesador"]
            pc.placa_de_video = info["placa_de_video"]
            pc.fuente_de_poder = info["fuente_de_poder"]
            pc.gabinete = info["gabinete"]
            pc.save()
            return redirect(PcArmadas)
            
    
    return render(request, "AppsDePag/EditarPc.html", {"formulario": formulario, "pc": pc})

def VerPc(request, id):
    pc = PcArmada.objects.get(id=id)
    return render(request, "AppsDePag/VerPc.html", {"pc": pc})
