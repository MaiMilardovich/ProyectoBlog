from django.shortcuts import render
from AppBlog.models import *
from AppBlog.forms import *
from django.http import HttpResponse

# Create your views here.

def inicio (request):

    return render (request, "AppBlog/inicio.html")


def lugar (request):

    return render (request, "AppBlog/salones.html")


def vestidos (request):

    return render (request, "AppBlog/vestidos.html")


def proveedores (request):

    return render (request, "AppBlog/proveedores.html")


def formulariosInicio (request):

    return render (request, "AppBlog/padreForm.html")


def formularioLugar (request):
    if request.method == "POST": #Si le doy a Enviar Informacion
        form1 = FormularioLugar (request.POST)
        if form1.is_valid(): # comprobar que no hay errores
            info = form1.cleaned_data
            lugarF = Lugar(nombre=info["nombre"], ciudad=info["ciudad"], pais=info["pais"], ) #lee la info de las cajas de texto (s/ cada formulario)
            lugarF.save() # guarda los datos en la base de datos
            return render(request, "AppBlog/inicio.html") # vuelve a mostrar lo que le digo dps de darle enviar a la info
    else:
        form1=FormularioLugar() #mostrar formulario vacio
    return render(request, "AppBlog/salonesForm.html", {"form1":form1}) # Apenas entro al URL


def formularioVestidos (request):
    if request.method == "POST": #Si le doy a Enviar Informacion
        form2 = FormularioVestidos (request.POST)
        if form2.is_valid(): # comprobar que no hay errores
            info = form2.cleaned_data
            vestidoF = Vestidos(diseñador=info["diseñador"], estilo=info["estilo"]) #lee la info de las cajas de texto (s/ cada formulario)
            vestidoF.save() # guarda los datos en la base de datos
            return render(request, "AppBlog/inicio.html") # vuelve a mostrar lo que le digo dps de darle enviar a la info
    else:
        form2=FormularioVestidos() #mostrar formulario vacio
    return render(request, "AppBlog/vestidosForm.html", {"form2":form2}) # Apenas entro al URL


def formularioProveedores (request):
    if request.method == "POST": #Si le doy a Enviar Informacion
        form3 = FormularioProveedor (request.POST)
        if form3.is_valid(): # comprobar que no hay errores
            info = form3.cleaned_data
            provF = Proveedores(proveedor=info["proveedor"], tipo=info["tipo"], mail=info["mail"],) #lee la info de las cajas de texto (s/ cada formulario)
            provF.save() # guarda los datos en la base de datos
            return render(request, "AppBlog/inicio.html") # vuelve a mostrar lo que le digo dps de darle enviar a la info
    else:
        form3=FormularioProveedor() #mostrar formulario vacio
    return render(request, "AppBlog/proveedorForm.html", {"form3":form3}) # Apenas entro al URL


def busquedas (request):

    return render (request, "AppBlog/padreBusqueda.html")


def buscarSalon (request):

    return render (request, "AppBlog/buscarSalon.html")


def buscandoSalon (request):

    if request.GET["ciudad"]:
        
        ciudad = request.GET["ciudad"]
        nombre = Lugar.objects.filter(ciudad__icontains=ciudad)

        return render(request, "AppBlog/resultadoSalon.html" , {"nombre": nombre    , "ciudad": ciudad})

    else:

        mensaje = "Regrese atras e ingrese un dato para buscar"

    return HttpResponse (mensaje)


def buscarVestido (request):

    return render (request, "AppBlog/buscarVestido.html")


def buscandoVestido (request):

    if request.GET["estilo"]:
        
        estilo = request.GET["estilo"]
        diseñador = Vestidos.objects.filter(estilo__icontains=estilo)

        return render(request, "AppBlog/resultadoVestido.html" , {"diseñador": diseñador   , "estilo": estilo})

    else:

        mensaje = "Regrese atras e ingrese un dato para buscar"

    return HttpResponse (mensaje)


def buscarProveedor (request):

    return render (request, "AppBlog/buscarProveedor.html")


def buscandoProveedor (request):

    if request.GET["tipo"]:
        
        tipo = request.GET["tipo"]
        nombre = Proveedores.objects.filter(tipo__icontains=tipo)

        return render(request, "AppBlog/resultadoProveedor.html" , {"nombre": nombre   , "tipo": tipo})

    else:

        mensaje = "Regrese atras e ingrese un dato para buscar"

    return HttpResponse (mensaje)