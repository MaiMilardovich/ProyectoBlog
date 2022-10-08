from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class FormularioLugar (forms.Form):   
    
    nombre = forms.CharField()
    ciudad = forms.CharField()
    pais = forms.CharField()


class FormularioVestidos (forms.Form):

    autor = forms.CharField()
    diseñador = forms.CharField()
    estilo = forms.CharField()
    fecha = forms.DateField()
    imagen = forms.ImageField()


class FormularioProveedor (forms.Form):

    proveedor = forms.CharField()
    tipo = forms.CharField()
    mail = forms.EmailField()    


class FormularioRegistro(UserCreationForm):

    email = forms.EmailField(label="Ingrese su correo")
    password1 = forms.CharField(label="Ingrese una constraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repita la constraseña", widget = forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username" , "email" , "password1" , "password2"] 