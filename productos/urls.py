from django.urls import path
from . import views

urlpatterns = [
    path("portatiles/", views.Portatiles.as_view(), name="Portatiles"),
    path("portatiles/crear/", views.CrearPortatil.as_view(), name="CrearPortatil"),
    path("portatiles/<int:pk>/", views.VerPortatil.as_view(), name="VerPortatil"),
    path("portatiles/editar/<int:pk>/", views.EditarPortatil.as_view(), name="EditarPortatil"),
    path("portatiles/eliminar/<int:pk>/", views.EliminarPortatil.as_view(), name="EliminarPortatil"),
]
