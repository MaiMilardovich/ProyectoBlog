from django.urls import path
from AppBlog.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("", inicio , name = "Inicio"),
    path("AboutUs", aboutus , name = "AboutUs"),
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
    path("login" , iniciar_sesion , name="Login"), 
    path("logout" , LogoutView.as_view (template_name="AppBlog/logout.html") , name="Logout"),
    path("registro" , registro , name="Registro"),
    path("editarUsuario", editarUsuario , name ="EditarUsuario"),
    path("editarVestido/<diseñadorNombre>", editarVestidos , name = "EditarVestidos"),


    path("Vestidos/borrar/<int:pk>" , VestidoBorrar.as_view(), name = "BorrarVestido"),
   




]
