from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .models import Portatil
from django.urls import reverse_lazy


class Portatiles(ListView):
    model = Portatil
    template_name = "productos/Portatiles.html"
    context_object_name = "Portatiles"
    
class CrearPortatil(CreateView):
    model = Portatil
    template_name = "productos/CrearPortatiles.html"
    success_url = reverse_lazy("Portatiles")
    fields = ["marca", "modelo", "spects"]
    
    
class EditarPortatil(UpdateView):
    ...

class VerPortatil(DetailView):
    model = Portatil
    template_name = "productos/VerPortatiles.html"    
