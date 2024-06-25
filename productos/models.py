from django.db import models

# Create your models here.

class Portatil(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    spects = models.CharField(max_length=500)
   
    def __str__(self):
        return f"Portatil {self.marca} {self.modelo} {self.spects}"    
