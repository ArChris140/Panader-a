"""
URL configuration for panaderia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tiendaApp import views

# Importa la función auth_login desde django.contrib.auth
from django.contrib.auth import login as auth_login

# para enviar mail
from django.urls import include, path

urlpatterns = [
    path('', views.listadoProducto, name='listadoProducto'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='Add'),
    path('agregarpro/<int:producto_id>/', views.agregar_producto2, name='Add2'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='Del'),
    path('restar/<int:producto_id>/', views.restar_producto, name='Sub'),
    path('limpiar/', views.limpiar_carrito, name='CLS'),
    path('comprar/', views.comprar_producto, name='COM'),
    path('contact/', views.correo, name='contact'),
    path('carro/', views.carro, name='carro'),
    path('login/', views.login, name='login'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('cerrar_sesion/', views.cerrarSesion, name='cerrar_sesion'),
    path('pago/', views.pago, name='pago'),
    path('admin/', admin.site.urls, name='admin'),
    path('custom-admin/', views.custom_admin, name='custom_admin'),
    path('verify-code/', views.verify_code, name='verify_code'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('mod_productos/', views.mod_productos, name='mod_productos'),
    path('modificar/<int:producto_id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('guardar_modificacion/<int:producto_id>/', views.guardar_modificacion, name='guardar_modificacion'),
    path('Historial-de-compras/', views.historialCompras, name='HistorialCompras'),
    path('verify-code/', views.verify_code_user, name='verify_code_user'),
]


