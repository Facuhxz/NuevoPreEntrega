from django.db import models


# IGNORAR ESTE MODEL, SE USO PARA PRUEBA
# class MotherBoard(models.Model):
#     modelo = models.CharField(max_length=25)
#     marca = models.CharField(max_length=25)
    
#     def __str__(self):
#         return f"Mother {self.marca} {self.modelo}"
        
# MODEL UTILIZADO PARA LA PAG FINAL
class PcArmada(models.Model):
    pc = models.CharField(max_length=10, default="")
    mother = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    placa_de_video = models.CharField(max_length=50)
    fuente_de_poder = models.CharField(max_length=50)
    gabinete = models.CharField(max_length=50)
    
    def __str__(self):
        return f"PC GAMER {self.pc} {self.mother} {self.ram} {self.procesador} {self.placa_de_video} {self.fuente_de_poder} {self.gabinete}"
