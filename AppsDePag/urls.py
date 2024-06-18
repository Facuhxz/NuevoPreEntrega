from django.urls import path
from AppsDePag import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("arma/tu/pc", views.ArmarPc, name="ArmarPc"),
    path("pc/armadas", views.PcArmadas, name="Pc Armadas")
]