from django import forms


class FormularioLugar (forms.Form):   
    
    nombre = forms.CharField()
    ciudad = forms.CharField()
    pais = forms.CharField()


class FormularioVestidos (forms.Form):

    diseñador = forms.CharField()
    estilo = forms.CharField()


class FormularioProveedor (forms.Form):

    proveedor = forms.CharField()
    tipo = forms.CharField()
    mail = forms.EmailField()    