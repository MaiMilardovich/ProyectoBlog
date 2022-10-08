from django.shortcuts import render
from AppBlog.models import *
from AppBlog.forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def inicio (request):

    return render (request, "AppBlog/inicio.html")

def aboutus (request):

    return render (request, "AppBlog/aboutUs.html")


@login_required
def lugar (request):

    return render (request, "AppBlog/salones.html")

@login_required
def vestidos (request):

    diseñadores = Vestidos.objects.all()

    return render (request, "AppBlog/vestidos.html" , {"resultado" : diseñadores})

@login_required
def editarVestidos (request, diseñadorNombre):

    diseñador = Vestidos.objects.get(diseñador=diseñadorNombre)

    if request.method == "POST":
       
        formularioEditar = FormularioVestidos (request.POST , request.FILES)

        if formularioEditar.is_valid(): # comprobar que no hay errores

            info = formularioEditar.cleaned_data

            diseñador.autor = info["autor"]
            diseñador.diseñador = info["diseñador"] #actualizar la info antigua por la que aparece en la caja de texto
            diseñador.estilo = info["estilo"] #Entre [] corresponde al form 
            diseñador.fechaCarga = info["fecha"]
            diseñador.imagen = info["imagen"]
            
            diseñador.save()

            return render(request, "AppBlog/inicio.html") # vuelve a mostrar lo que le digo dps de darle enviar a la info

    else:

        formularioEditar=FormularioVestidos(initial= {"diseñador": diseñador.diseñador , "estilo":diseñador.estilo}) #mostrar formulario con los datos (ya no vacio)
    
    return render(request, "AppBlog/editarVestidos.html", {"formulario":formularioEditar, "diseñadorNombre": diseñadorNombre })

class VestidoBorrar(DeleteView, LoginRequiredMixin):
    model= Vestidos
    success_url = "/AppBlog/"


@login_required
def proveedores (request):

    return render (request, "AppBlog/proveedores.html")

@login_required
def formulariosInicio (request):

    return render (request, "AppBlog/padreForm.html")

@login_required
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

@login_required
def formularioVestidos (request):
    if request.method == "POST": #Si le doy a Enviar Informacion
        form2 = FormularioVestidos (request.POST , request.FILES)
        if form2.is_valid(): # comprobar que no hay errores
            info = form2.cleaned_data
            vestidoF = Vestidos(diseñador=info["diseñador"], estilo=info["estilo"], imagen=info["imagen"] ) #lee la info de las cajas de texto (s/ cada formulario)
            vestidoF.save() # guarda los datos en la base de datos
            return render(request, "AppBlog/inicio.html") # vuelve a mostrar lo que le digo dps de darle enviar a la info
    else:
        form2=FormularioVestidos() #mostrar formulario vacio
    return render(request, "AppBlog/vestidosForm.html", {"form2":form2}) # Apenas entro al URL

@login_required
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

@login_required
def busquedas (request):

    return render (request, "AppBlog/padreBusqueda.html")

@login_required
def buscarSalon (request):

    return render (request, "AppBlog/buscarSalon.html")

@login_required
def buscandoSalon (request):

    if request.GET["ciudad"]:
        
        ciudad = request.GET["ciudad"]
        nombre = Lugar.objects.filter(ciudad__icontains=ciudad)

        return render(request, "AppBlog/resultadoSalon.html" , {"nombre": nombre    , "ciudad": ciudad})

    else:

        mensaje = "Regrese atras e ingrese un dato para buscar"

    return HttpResponse (mensaje)

@login_required
def buscarVestido (request):

    return render (request, "AppBlog/buscarVestido.html")

@login_required
def buscandoVestido (request):

    if request.GET["estilo"]:
        
        estilo = request.GET["estilo"]
        diseñador = Vestidos.objects.filter(estilo__icontains=estilo)
        imagen = Vestidos.objects.filter(estilo__icontains=estilo)

        return render(request, "AppBlog/resultadoVestido.html" , {"diseñador": diseñador   , "estilo": estilo , "imagen": imagen})

    else:

        mensaje = "Regrese atras e ingrese un dato para buscar"

    return HttpResponse (mensaje)

@login_required
def buscarProveedor (request):

    return render (request, "AppBlog/buscarProveedor.html")

@login_required
def buscandoProveedor (request):

    if request.GET["tipo"]:
        
        tipo = request.GET["tipo"]
        nombre = Proveedores.objects.filter(tipo__icontains=tipo)

        return render(request, "AppBlog/resultadoProveedor.html" , {"nombre": nombre   , "tipo": tipo})

    else:

        mensaje = "Regrese atras e ingrese un dato para buscar"

    return HttpResponse (mensaje)


#Iniciar sesion

def iniciar_sesion(request):

    if request.method == "POST": #Click al boton inciiar sesion

        form =  AuthenticationForm (request, data=request.POST)

        if form.is_valid(): # comprobar que no hay errores

            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contraseña)

            if user: # usuario existe 

                login(request, user)

                return render(request, "AppBlog/inicio.html" , {"mensaje":f" Bienvenida Bride to be: {user}"})

        else: #datos incorrectos

            return render(request, "AppBlog/inicio.html" , {"mensaje": f"Datos incorrectos. Vuelva a intentarlo"})

    else: 

        form = AuthenticationForm ()

    return render (request, "AppBlog/login.html", {"form": form})

#Registrar nuevo usuario

def registro(request):

    if request.method == "POST":

        form = FormularioRegistro(request.POST)

        # form = UserCreationForm(request.POST) --> ANTES DE CREAR UN FORM EN froms.py

        if form.is_valid():

            nombreUsuario = form.cleaned_data["username"]

            form.save()

            return render (request, "AppBlog/inicio.html" , {"mensaje":f"Bride to be {nombreUsuario} creada"})

    else:

        form = FormularioRegistro()
        # form = UserCreationForm() --> ANTES DE CREAR UN FORM EN froms.py
    
    return render(request, "AppBlog/registro.html", {"form" : form})

# Modificar usuario existente

@login_required # No puedo editar el usuario si no inicia sesion
def editarUsuario(request):

    usuario = request.user # Para saber que usuario esta conectado

    if request.method == "POST": # si le doy clik al boton editar
       
        formeditar = FormularioRegistro (request.POST)

        if formeditar.is_valid(): # comprobar que no hay errores

            info = formeditar.cleaned_data
            
            usuario.username = info["username"] 
            usuario.email = info["email"] 
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"] 

            usuario.save()

            return render(request, "AppBlog/inicio.html") 

    else:

        formeditar=FormularioRegistro(initial= {"username":usuario.username,"email": usuario.email }) 
    
    return render(request, "AppBlog/editarUsuario.html", {"formeditar":formeditar, "usuario": usuario })

