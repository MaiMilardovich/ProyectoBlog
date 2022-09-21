from django.urls import path
from AppBlog.views import *



urlpatterns = [
    path("", inicio , name = "Inicio"),
    path("Salones/", lugar , name = "Salones"),
    path("Vestidos/", vestidos , name = "Vestidos"),
    path("Proveedores/", proveedores , name = "Proveedores"),
    path("Formularios/", formulariosInicio , name = "Formularios"),
    path("FormularioSalones/", formularioLugar , name = "FormularioSalon"),
    path("FormularioVestidos/", formularioVestidos , name = "FormularioVestidos"),
    path("FormularioProveedores/", formularioProveedores , name = "FormularioProveedores"),
    path("Busquedas/", busquedas , name = "Busquedas"), 
    path("BuscarSalon/", buscarSalon , name = "BuscarSalon"), 
    path("BuscandoSalon/", buscandoSalon ),    
    path("BuscarVestido/", buscarVestido , name = "BuscarVestido"), 
    path("BuscandoVestido/", buscandoVestido ),  
    path("BuscarProveedor/", buscarProveedor , name = "BuscarProveedor"), 
    path("BuscandoProveedor/", buscandoProveedor ),  


]
