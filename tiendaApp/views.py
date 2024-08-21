from django.shortcuts import render, redirect
from .serializers import ProductoSerializer, UsuarioSerializer
from django.urls import reverse
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from tiendaApp.forms import FormProducto, FormUsuario, FormCompra, FormCantidad
from tiendaApp.models import Producto, Usuario, Cantidad, Compra
from tiendaApp.carrito import Carrito
from tiendaApp.context_processor import total_carrito
from django.forms.utils import ErrorList
from django.contrib.auth import authenticate, logout, login as auth_login
from .models import Usuario
from django.contrib import messages
import random
import string
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
# Para enviar mail
from django.core.mail import EmailMessage
from .forms import FormularioContacto
from django.http import HttpResponse




def listadoProducto(request):
    producto = Producto.objects.all()
    data = {'producto': producto}

    if request.user.is_authenticated:
        data['user_email'] = request.user.email

    return render(request, 'index.html', data)

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect(reverse('listadoProducto'))

def agregar_producto2(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect(reverse('carro'))

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect(reverse('carro'))

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect(reverse('carro'))

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(reverse('carro'))

def comprar_producto(request):
    carrito = Carrito(request)
    current_user = 2
    if request.method == 'POST':
        form = FormCompra(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.Precio_Total = total_carrito(request)
            post.Id_Usuario = current_user
            post.save()
            carrito.limpiar()
    return redirect(reverse('listadoProducto'))

def contact(request):
    return render(request,'contact.html')

def carro(request):
    return render(request, 'carro.html')


def login(request):
    if request.method == 'POST':
        try:
            detalleUsuario = Usuario.objects.get(Correo=request.POST['correo'], Contraseña=request.POST['password'])
            print("usuario=", Usuario)
            request.session['Correo'] = detalleUsuario.Correo
            return redirect('listadoProducto')
        except Usuario.DoesNotExist as e:
            messages.success(request, 'Email de usuario o contraseña incorrecta')
    return render(request, 'login.html')

def cerrarSesion(request):
    logout(request)
    return redirect('listadoProducto')


def quienes_somos (request):
    return render (request,'quienes_somos.html')


def crear_usuario(request):
    error_message = ''

    if request.method == 'POST':
        form = FormUsuario(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['Correo']
            if Usuario.objects.filter(Correo=correo).exists():
                error_message = 'Ya existe un usuario con este correo electrónico.'
            else:
                # Guardar el formulario solo si no hay usuarios con el mismo correo y la contraseña tiene al menos 8 caracteres
                user = form.save(commit=False)
                user.save()

                # Generar y enviar el código de verificación
                verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                send_mail(
                    'Código de verificación',
                    f'Tu código de verificación es: {verification_code}',
                    settings.DEFAULT_FROM_EMAIL,
                    [correo],
                    fail_silently=False,
                )
                request.session['verification_code'] = verification_code
                request.session['email'] = correo

                return redirect('verify_code_user')  # Redirige a la verificación del código para el usuario

    else:
        form = FormUsuario()

    return render(request, 'sing-in.html', {'form': form, 'error_message': error_message})

@login_required(login_url='/login/')

@login_required(login_url='/login/')
def verify_code_user(request):
    if request.method == 'POST':
        entered_code = request.POST['verification_code']
        stored_code = request.session.get('verification_code')

        if entered_code == stored_code:
            email = request.session.get('email')
            user = authenticate(request, username=email, password='dummy_password')
            auth_login(request, user)
            return redirect('listadoProducto')  # Redirige a la página deseada después de la verificación
        else:
            return render(request, 'verify_code_user.html', {'error': 'Código incorrecto'})

    return render(request, 'verify_code_user.html')



def pago(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Validar que la hora seleccionada esté dentro del rango permitido
            selected_time = form.cleaned_data['time']
            min_time = datetime.time(8, 0)
            max_time = datetime.time(19, 0)

            if min_time <= selected_time <= max_time:
                # Hora válida, redirigir a la página principal con mensaje de confirmación
                messages.success(request, '¡Gracias por tu compra!')
                return redirect('listadoProducto')  # Reemplaza 'listadoProducto' con la URL real
            else:
                messages.error(request, 'Selecciona una hora válida entre las 8 AM y las 7 PM.')
    else:
        form = CheckoutForm()

    return render(request, 'pago.html')








def correo(request):

    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre").upper()
            email=request.POST.get("email").upper()
            mensaje=request.POST.get("mensaje")

            email=EmailMessage("Mensaje del formulario de contacto",
            "El usuario con el nombre: {} con el correo electronico: {} escribe lo siguiente:\n\n {}".format(nombre, email, mensaje), 
            '',
            ["Shiros.panad@gmail.com"], 
            reply_to=[email])

            try:
                email.send()

                return redirect("/contact/?valido")
            except:
                return redirect("/contact/?novalido")

    return render(request, "contact.html", {'miFormulario':formulario_contacto})

def custom_admin(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)

        # Autenticar al usuario
        user = authenticate(request, username=usuario, password=password, email=email)

        if user is not None and user.is_superuser:
            verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            send_mail(
                'Código de verificación',
                f'Tu código de verificación es: {verification_code}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            request.session['verification_code'] = verification_code
            request.session['email'] = email

            # Autenticar al usuario directamente después de enviar el código
            auth_login(request, user)

            print('Usuario autenticado y código de verificación enviado')
            return redirect('verify_code')
            
        else:
            # Usuario no autenticado o no es un superusuario
            print('Credenciales incorrectas')
            return render(request, 'admin.html', {'error': 'Credenciales incorrectas'})

    return render(request, 'admin.html')

@login_required(login_url='/custom_admin/')
def verify_code(request):
    if request.method == 'POST':
        entered_code = request.POST['verification_code']
        stored_code = request.session.get('verification_code')

        if entered_code == stored_code:
            email = request.session.get('email')
            user = authenticate(request, username=email, password='dummy_password')
            auth_login(request, user)
            return redirect('admin_home')
        else:
            return render(request, 'verify_code.html', {'error': 'Código incorrecto'})

    return render(request, 'verify_code.html')

@login_required(login_url='custom-admin')
def admin_home(request):
    # Tu vista de la página de admin aquí
    return render(request, 'admin_home.html')


def mod_productos(request):
    productos = Producto.objects.all()
    return render(request, 'modProductos.html', {'productos': productos})

def modificar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    # Puedes agregar la lógica de modificación aquí si es necesario
    return render(request, 'modificar_producto.html', {'producto': producto})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return HttpResponseRedirect(reverse('mod_productos'))

def modificar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'modificar_producto.html', {'producto': producto})

def guardar_modificacion(request, producto_id):
    # Obtiene el producto existente
    producto = get_object_or_404(Producto, id=producto_id)

    # Actualiza los campos con los datos del formulario
    producto.Nombre = request.POST.get('nombre')
    producto.Precio = request.POST.get('precio')
    producto.Descripcion = request.POST.get('descripcion')
    producto.Stock = request.POST.get('stock')

    # Guarda los cambios
    producto.save()

    # Devuelve una respuesta JSON
    return JsonResponse({'status': 'success'})
    
@login_required(login_url='login')
def historialCompras(request):
    print(request.user)
    return render(request, 'historialCompras.html')