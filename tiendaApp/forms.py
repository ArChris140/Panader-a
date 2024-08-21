from django import forms
from tiendaApp.models import Producto, Usuario, Compra, Cantidad
from django.core.validators import MinLengthValidator
from .models import Usuario
from django.core.exceptions import ValidationError

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {'Contraseña': forms.PasswordInput()}

class FormCompra(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

class FormCantidad(forms.ModelForm):
    class Meta:
        model = Cantidad
        fields = '__all__'

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)    

# aqui comienza la clase para enviar mail

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label='Nombre', required=True, max_length=20)
    email=forms.CharField(label='Email', required=True, max_length=30)
    mensaje=forms.CharField(label='mensaje', max_length=400, widget=forms.Textarea )

# aqui termina la clase para enviar mail