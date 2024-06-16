from django.urls import path
from AppsDePag import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("crear/mother/", views.creacion_de_mother_v2, name="crearV2")
]