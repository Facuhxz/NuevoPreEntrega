from django.db import models


class MotherBoard(models.Model):
    modelo = models.CharField(max_length=25)
    marca = models.CharField(max_length=25)
    
    def __str__(self):
        return f"Mother {self.marca} {self.modelo}"
        

