from django.urls import path
from AppsDePag import views


# URLS ACTIVAS EN LA PAG
urlpatterns = [
    path("", views.inicio, name="inicio"),  
    path("arma/tu/pc", views.ArmarPc, name="ArmarPc"), 
    path("pc/armadas", views.PcArmadas, name="Pc Armadas")
]